from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_db
from services.user_service import UserService
from dao.user_dao import UserDAO
from schemas.user_schema import UserCreate
from utils.auth import create_access_token, authenticate_user
from fastapi.security import OAuth2PasswordRequestForm

user_router = APIRouter()

@user_router.post(
    "/signup",
    summary="Register a new user",
    description="Creates a new user account with a unique username and password."
)
async def signup(user: UserCreate, db: AsyncSession = Depends(get_db)):
    service = UserService(UserDAO(db))
    existing = await service.get_user(user.username)
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    await service.create_user(user.username, user.password)
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@user_router.post(
    "/login",
    summary="User login and JWT token generation",
    description="Authenticates a user and returns a JWT access token for use in protected endpoints."
)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    user = await authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}