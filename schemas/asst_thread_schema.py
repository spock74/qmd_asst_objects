from typing import Dict
from pydantic import BaseModel, Field

class ThreadSchema(BaseModel):
    id: int = Field(..., description="Unique identifier integer sequential for the thread")
    thread_id: str = Field(..., description="Unique identifier for the thread returned when the thread was created")
    object: str = Field(..., description="Object type")
    created_at: int = Field(..., description="Timestamp of when the thread was created")
    metadata_: Dict[str, str] = Field({}, description="Metadata associated with the thread")
    