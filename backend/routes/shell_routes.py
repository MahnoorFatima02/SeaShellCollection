from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from services.shell_service import ShellService
from dao.shell_dao import ShellDAO
from database.db import get_db
from schemas.shell_schemas import ShellCreate, ShellUpdate, ShellRead, SuggestResponse
from utils.auth import get_current_user
import openai
import httpx
from pydantic import BaseModel
from utils.llm_helpers import get_response_from_llm
import os

class SuggestRequest(BaseModel):
    keyword: str
 
shell_router = APIRouter()

@shell_router.get(
    "/shells",
    summary="List all shells (public)",
    description="Returns a list of all shells in the collection.",
    response_model=List[ShellRead],
    status_code=status.HTTP_200_OK,
)
async def get_shells(db: AsyncSession = Depends(get_db)) -> List[ShellRead]:
    """Get all shells."""
    service = ShellService(ShellDAO(db))
    return await service.get_all_shells()

@shell_router.get(
    "/shells/{id}",
    summary="Get shell by ID (protected)",
    description="Returns a single shell by its unique ID. Requires authentication.",
    response_model=ShellRead,
    status_code=status.HTTP_200_OK,
)
async def get_shell(
    id: int,
    db: AsyncSession = Depends(get_db),
    user=Depends(get_current_user)
) -> ShellRead:
    """Get a shell by its ID."""
    service = ShellService(ShellDAO(db))
    return await service.get_shell(id)

@shell_router.post(
    "/shells",
    summary="Create a new shell (protected)",
    description="Creates a new shell entry in the collection. Requires authentication.",
    response_model=ShellRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_shell(
    shell: ShellCreate,
    db: AsyncSession = Depends(get_db),
    user=Depends(get_current_user)
) -> ShellRead:
    """Create a new shell."""
    service = ShellService(ShellDAO(db))
    return await service.create_shell(shell.dict())

@shell_router.put(
    "/shells/{id}",
    summary="Update a shell (protected)",
    description="Updates an existing shell entry by its ID. Requires authentication.",
    response_model=ShellRead,
    status_code=status.HTTP_200_OK,
)
async def update_shell(
    id: int,
    shell: ShellUpdate,
    db: AsyncSession = Depends(get_db),
    user=Depends(get_current_user)
) -> ShellRead:
    """Update a shell by its ID."""
    service = ShellService(ShellDAO(db))
    return await service.update_shell(id, shell.dict(exclude_unset=True))

@shell_router.delete(
    "/shells/{id}",
    summary="Delete a shell (protected)",
    description="Deletes a shell entry by its ID. Requires authentication.",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_shell(
    id: int,
    db: AsyncSession = Depends(get_db),
    user=Depends(get_current_user)
) -> Response:
    """Delete a shell by its ID."""
    service = ShellService(ShellDAO(db))
    await service.delete_shell(id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@shell_router.post(
    "/shells/creative",
    summary="Suggest a seashell based on a keyword using OpenAI",
    response_model=SuggestResponse,
    status_code=status.HTTP_200_OK,
)
async def suggest_shell_gbif(req: SuggestRequest):
    """
    Create a seashell species name or type that matches the given keyword using OpenAI.
    """
    prompt = (
        f"Suggest a fictional seashell name and description based on keyword: '{req.keyword}'"
    )
    response = await get_response_from_llm(prompt)
    return SuggestResponse(suggestion=response.get("generated_text", "No suggestion"))


@shell_router.post(
    "/shells/suggest",
    summary="Suggest a seashell species based on a keyword using GBIF",
    response_model=SuggestResponse,
    status_code=status.HTTP_200_OK,
)

async def suggest_shell_gbif(req: SuggestRequest):
    mollusk_taxon_key = 52  # Mollusca
    url = f"https://api.gbif.org/v1/species/search?q={req.keyword}&limit=10&higherTaxonKey={mollusk_taxon_key}"
    async with httpx.AsyncClient() as client:
        gbif_response = await client.get(url)
        if gbif_response.status_code != 200:
            raise HTTPException(status_code=500, detail="GBIF API error")
        data = gbif_response.json()
        seen = set()
        suggestions = []
        for result in data.get("results", []):
            name = f"{result.get('scientificName', 'Unknown')} ({result.get('canonicalName', '')})"
            if name not in seen:
                seen.add(name)
                suggestions.append(name)
            if len(suggestions) == 5:
                break
        if not suggestions:
            suggestions = ["No seashell species found for that keyword."]
        return SuggestResponse(suggestions=suggestions)