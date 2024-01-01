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


# The file object
# https://platform.openai.com/docs/api-reference/files/object
# The File object represents a document that has been uploaded to OpenAI.
# {
#   "id": "file-abc123",
#   "object": "file",
#   "bytes": 120000,
#   "created_at": 1677610602,
#   "filename": "salesOverview.pdf",
#   "purpose": "assistants",
# }
class FileObjectSchema(BaseModel):
    file_id: str
    object: str
    bytes: int
    created_at: int
    filename: str
    purpose: str


class FileSchemaBase(BaseModel):
    file_object: FileObjectSchema = Field(..., description="File object")
    assistant_id: str = Field(..., description="Unique identifier for the assistant")
    created_by: UUID4 = Field(..., description="User that created the file")
    file_extension: str = Field(..., description="Extension of the file")


class FileSchema(FileSchemaBase):
    id: int = Field(..., description="ID autoincrement of the file")
    custom_uuid: UUID4 = Field(..., description="Unique identifier for the file")
    file_id: str = Field(..., description="Unique identifier for the file")
    object: str = Field(..., description="Object type")
    created_at: int = Field(..., description="Timestamp of when the file was created")
    deleted_at: int = Field(..., description="Timestamp of when the file was deleted")
    deleted_by: UUID4 = Field(..., description="User that deleted the file")


    class Config:
        orm_mode = True
        