from pydantic import BaseModel, Field, UUID4
from typing import Optional, List, Union ,  Dict
import uuid
from datetime import datetime


class AssistantInstructionsSchema(BaseModel):
    id: int = Field(..., description="ID autoincrement of the assistant")
    custom_uuid: UUID4 = Field(..., description="UUID of the assistant")
    instructions: str = Field(..., description="Instructions for the assistant at its creation. Liied to 32768 characters")
    created_at: datetime = Field(..., description="Timestamp when the instructions were created")
    
    
    class Config:
        orm_mode = True