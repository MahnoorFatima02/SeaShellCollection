from pydantic import BaseModel, constr, ConfigDict
from typing import Optional, List

class ShellCreate(BaseModel):
    name: constr(min_length=1, strict=True)
    species: constr(min_length=1, strict=True)
    description: constr(min_length=1, strict=True)
    location: Optional[str] = None
    size: constr(min_length=1, strict=True)

class ShellUpdate(BaseModel):
    name: Optional[constr(min_length=1,strict=True)] = None
    species: Optional[constr(min_length=1, strict=True)] = None
    description: Optional[constr(min_length=1, strict=True)] = None
    location: Optional[str] = None
    size: Optional[constr(min_length=1, strict=True)] = None

class ShellRead(BaseModel):
    id: int
    name: str
    species: str
    description: Optional[str] = None
    location: Optional[str] = None
    size: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
   
    
class SuggestResponse(BaseModel):
    suggestions: List[str]