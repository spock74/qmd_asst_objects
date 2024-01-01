# ----------------------------------------------------------------------
# https://platform.openai.com/docs/api-reference/runs/object
# ----------------------------------------------------------------------
#
# Represents an execution run on a thread.
#

from pydantic import BaseModel, Field, UUID4, PositiveInt, DateTime, Email
from typing import Optional, List, Union ,  Dict
import uuid
from datetime import datetime

class AssistantRunSchemaBase(BaseModel):
    run_id: str = Field(..., description="Unique identifier for the assistant")
    object: str = Field(..., description="Object type")
    assistant_id: str = Field(..., description="Unique identifier for the assistant")
    thread_id: str = Field(..., description="Unique identifier for the thread")
    model: str = Field(..., description="The model used for the run")
    instructions: str = Field(..., description="The instructions used for the run")
    tools: List[Dict] = Field(..., description="List of tools to be used by the assistant")
    file_ids: List[str] = Field(..., description="List of file IDs to be used by the assistant, each one returned by the OpenAI API create")
    metadata_: str = Field(..., description="The metadata used for the run")
    run_started_by: UUID4 = Field(..., description="User [human or another AI component such as another asssistant] that started this running")

class AssistantRunSchemaRunning(AssistantRunSchemaBase):
    status: str = Field(..., description="Status of the run")
    started_at: int = Field(..., description="Timestamp of when the run was started")
    expires_at: int = Field(..., description="Timestamp of when the run will expire")
    cancelled_at: int = Field(..., description="Timestamp of when the run was cancelled")
    failed_at: int = Field(..., description="Timestamp of when the run failed")
    completed_at: int = Field(..., description="Timestamp of when the run was completed")
    last_error: str = Field(..., description="Last error message")


class AssistantRunSchemaRetrieveStatus(AssistantRunSchemaRunning):
    checked_at: int = Field(..., description="Timestamp of when the run was last checked")
    checked_status: str = Field(..., description="Last check error message")
                                      

class AssistantRunSchemaInDB(AssistantRunSchemaRetrieveStatus):
    id: int = Field(..., description="ID autoincrement of the run")
    custom_uuid: UUID4 = Field(..., description="Unique identifier for the run")
    created_by: UUID4 = Field(..., description="User that created the run")
    created_at: int = Field(..., description="Timestamp of when the run was created")



    class Config:
        orm_mode = True