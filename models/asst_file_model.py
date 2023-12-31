from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import  relationship
from sqlalchemy.sql import func
import uuid
from sqlalchemy.dialects.postgresql import UUID
from core.configs import settings


class AssistanteFileModel(settings.DBBaseModel):
    __tablename__ = "assistant_files"

    id = Column(Integer, primary_key=True, autoincrement=True)
    custom_uuid = Column(UUID(as_uuid=True), nullable=False)
    assistance_file_id = Column(String, nullable=False, unique=True, index=True)
    object = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(UUID(as_uuid=True), ForeignKey('users.user_id'), nullable=False)
    assistant_id = Column(String, ForeignKey('assistants.assistant_id'), nullable=False)

    user = relationship('User', foreign_keys=[created_by])

    assistant = relationship('Assistant', foreign_keys=[assistant_id])
    