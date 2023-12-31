# -----------------------------------------------------------------------------
#https://platform.openai.com/docs/api-reference/messages/object
# -----------------------------------------------------------------------------
# {
#   "id": "msg_abc123",
#   "object": "thread.message",
#   "created_at": 1698983503,
#   "thread_id": "thread_abc123",
#   "role": "assistant",
#   "content": [
#     {
#       "type": "text",
#       "text": {
#         "value": "Hi! How can I help you today?",
#         "annotations": []
#       }
#     }
#   ],
#   "file_ids": [],
#   "assistant_id": "asst_abc123",
#   "run_id": "run_abc123",
#   "metadata": {}
# }

# from pydantic import BaseModel, Field, UUID4, PositiveInt, DateTime, Email
# from typing import Optional, List, Union ,  Dict
# import uuid
# from datetime import datetime



# class AssistantMessageSchemaBase(BaseModel):
#     thread_id: str = Field(..., description="Unique identifier for the thread")
#     role: str = Field(..., description="Role of whos speaking")
#     content
#     file_ids: List[str] = Field(..., description="List of file IDs to be used by the assistant, each one returned by the OpenAI API create file")
#     assistant_id: str = Field(..., description="ID of the assistant returned by the OpenAI API")
#     run_id: str = Field(..., description="ID of the run returned by the OpenAI API")
#     metadata_: dict = Field(..., description="Parameters of the model to be used by the assistant")

# class AssistantMessageSchema(AssistantMessageSchemaBase):
#     id: int = Field(..., description="ID autoincrement of the message")
#     object: str = Field(..., description="Object type of the message")
#     created_at: int = Field(..., description="Timestamp of when the message was created")


from typing import List, Optional, Dict
from pydantic import BaseModel, Field

class TextValue(BaseModel):
    value: str = Field(..., description="The actual text")
    annotations: List[str] = Field([], description="Annotations for the text")

class ContentType(BaseModel):
    type: str = Field(..., description="Type of the content")
    text: TextValue = Field(..., description="Text value of the content")

class MessageSchema(BaseModel):
    id: int = Field(..., description="Unique integer identifier integer sequential for the message")
    message_id: str = Field(..., description="Unique identifier for the message returned when the message was created")
    object: str = Field(..., description="Object type")
    created_at: int = Field(..., description="Timestamp of when the message was created")
    thread_id: str = Field(..., description="Unique identifier for the thread")
    role: str = Field(..., description="Role of the message sender")
    content: List[ContentType] = Field(..., description="Content of the message")
    file_ids: List[str] = Field([], description="List of file ids associated with the message")
    assistant_id: str = Field(..., description="Unique identifier for the assistant")
    run_id: str = Field(..., description="Unique identifier for the run")
    metadata_: Dict[str, str] = Field({}, description="Metadata associated with the message")
    
    class Config:
        orm_mode = True