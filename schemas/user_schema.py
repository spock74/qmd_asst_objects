from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from uuid import UUID
from datetime import datetime

class UserSchemaBase(BaseModel):
    name: str 
    surname: str 
    email: EmailStr 
    is_admin: bool = False
    tyoe_user: str 

class UserSchemaCreate(UserSchemaBase):
    password: str

class UserSchemaUpdate(UserSchemaBase):
    password: str  
    status: str = Field(..., description="Status of the user")
    updated_at: datetime = Field(..., description="Timestamp when the user was last updated")
    name: str = Field(..., alias="name")
    email: EmailStr = Field(..., alias="email")
    is_admin: bool = Field(..., alias="is_admin")
    type_user: str = Field(..., alias="type_user")

class UserSchemaInDB(UserSchemaBase):
    id: int = Field(..., alias="id")
    user_id: UUID = Field(..., alias="user_id") 
    created_at: datetime = Field(..., alias="created_at")


    class Config:
        orm_mode = True