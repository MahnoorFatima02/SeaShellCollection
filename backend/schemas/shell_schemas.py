from pydantic import BaseModel, constr, ConfigDict
from typing import Optional, List

class ShellCreate(BaseModel):
    name: constr(min_length=1)
    species: constr(min_length=1)
    description: constr(min_length=1)
    location: Optional[str] = None
    size: constr(min_length=1)

class ShellUpdate(BaseModel):
    name: Optional[constr(min_length=1)] = None
    species: Optional[constr(min_length=1)] = None
    description: Optional[constr(min_length=1)] = None
    location: Optional[str] = None
    size: Optional[constr(min_length=1)] = None

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