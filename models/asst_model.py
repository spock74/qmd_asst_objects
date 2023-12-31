from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import  relationship
from sqlalchemy.sql import func
import uuid
from sqlalchemy.dialects.postgresql import UUID
from core.configs import settings


class AssistantModel(settings.DBBaseModel):
    __tablename__ = 'assistants'

    object = Column(String, nullable=False)
    assistante_name = Column(String, nullable=False, unique=True)
    assistant_id =  Column(String, nullable=False, primary_key=True, unique=True, index=True)
    custom_uuid = Column(UUID(as_uuid=True), nullable=False)
    created_by = Column(UUID(as_uuid=True), ForeignKey('users.user_id'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    model = Column(String, nullable=False)
    metadata_ = Column(JSON, nullable=False)
    instructions = Column(Text, nullable=False)
    tools = Column(JSON, nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=False)
    updated_by = Column(UUID(as_uuid=True), ForeignKey('users.user_id'), nullable=False)
    
    user = relationship('User', foreign_keys=[created_by])
    