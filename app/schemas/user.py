from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    
    first_name: int = Field(..., max_length=30)

class UserRead(BaseModel):
    id: int
    name: str
