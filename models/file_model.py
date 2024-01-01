# ------------------------------------------------------------------------
#
# ------------------------------------------------------------------------


# {
#   "id": "file-abc123",
#   "object": "file",
#   "bytes": 120000,
#   "created_at": 1677610602,
#   "filename": "salesOverview.pdf",
#   "purpose": "assistants",
# }



from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import  relationship
from sqlalchemy.sql import func
import uuid
from sqlalchemy.dialects.postgresql import UUID
from core.configs import settings


class FileModel(settings.DBBaseModel):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, autoincrement=True)
    custom_uuid = Column(UUID(as_uuid=True), nullable=False)
    file_object = Column(JSON, nullable=False)
    object = Column(String(255), nullable=False)
    created_by = Column(UUID(as_uuid=True), ForeignKey('users.user_id'), nullable=False)
    assistant_id = Column(String, ForeignKey('assistants.assistant_id'), nullable=False)
    file_extension = Column(String, nullable=False)
    deleted_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    deleted_by = Column(UUID(as_uuid=True), ForeignKey('users.user_id'), nullable=True)

    user = relationship('User', foreign_keys=[created_by, deleted_by])

    assistant = relationship('Assistant', foreign_keys=[assistant_id])
    