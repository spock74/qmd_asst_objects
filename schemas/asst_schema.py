# ------------------------------------------------------------------
# https://platform.openai.com/docs/api-reference/assistants/object        
# ------------------------------------------------------------------


# ------ the asssistant object -------------------------------------
{
#   "id": "asst_abc123",
#   "object": "assistant",
#   "created_at": 1698984975,
#   "name": "Math Tutor",
#   "description": null,
#   "model": "gpt-4",
#   "instructions": "You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
#   "tools": [
#     {
#       "type": "code_interpreter"
#     }
#   ],
#   "file_ids": [],
#   "metadata": {}
}
# ------------------------------------------------------------------



from pydantic import BaseModel, Field, UUID4, PositiveInt, DateTime, Email
from typing import Optional, List, Union ,  Dict
import uuid
from datetime import datetime

class AssistantCreateSchema(BaseModel):
    intructions: UUID4 = Field(..., description="Instructions for the assistant at its creation. Limied to 32768 characters")
    tools: List[Dict] = Field(..., description="List of tools to be used by the assistant")
    assistant_name: str = Field(..., description="Name of the assistant")
    model = Field(..., description="Model ID to be used by the assistant")
    metadata_: dict = Field(..., description="Parameters of the model to be used by the assistant")
    file_ids: List[str] = Field(..., description="List of file IDs to be used by the assistant, each one returned by the OpenAI API create file")
    
class AssistantUpdateSchma(AssistantCreateSchema):
    updated_at: datetime = Field(..., description="Timestamp when the assistant was last updated")
    updated_by: UUID4 = Field(..., description="User that last updated the assistant")
    
class AssistantInDB(AssistantCreateSchema, AssistantUpdateSchma):
    id: int = Field(..., description="ID autoincrement of the assistant")
    object: str = Field(..., description="Object type of the assistant")
    custom_uuid: UUID4 = Field(..., description="UUID of the assistant")
    assistant_id: str = Field(..., description="ID of the assistant returned by the OpenAI API")    
    
    
    
    class Config:
        orm_mode = True
        
        
        
        
