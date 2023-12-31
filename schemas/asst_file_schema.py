# -----------------------------------------------------------------------------
# https://platform.openai.com/docs/api-reference/assistants/file-object
# {
#   "id": "file-abc123",
#   "object": "assistant.file",
#   "created_at": 1699055364,
#   "assistant_id": "asst_abc123"
# }
# -----------------------------------------------------------------------------

from pydantic import BaseModel, Field, UUID4, PositiveInt, DateTime, Email
from typing import Optional, List, Union ,  Dict
import uuid
from datetime import datetime



class AssistanteFileSchemaBase(BaseModel):
    assistant_id: str = Field(..., description="Unique identifier for the assistant")
    created_by: UUID4 = Field(..., description="User that created the file")


class AssistanteFileSchema(AssistanteFileSchemaBase):
    id: int = Field(..., description="ID autoincrement of the file")
    custom_uuid: UUID4 = Field(..., description="Unique identifier for the file")
    assistant_file_id: str = Field(..., description="Unique identifier for the file")
    object: str = Field(..., description="Object type")
    created_at: int = Field(..., description="Timestamp of when the file was created")


    class Config:
        orm_mode = True
        