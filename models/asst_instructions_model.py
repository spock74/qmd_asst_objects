
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import  relationship
from sqlalchemy.sql import func
import uuid
from sqlalchemy.dialects.postgresql import UUID
from core.configs import settings


class AssistantInstructionsModel(settings.DBBaseModel):
    __tablename__ = 'assistants_instructions'


    id = Column(Integer, primary_key=True, autoincrement=True)
    custom_uuid = Column(UUID(as_uuid=True), nullable=False)
    #! TODO creat a trigger to report error in tryind to insert a instruction greater than 32768 chars
    instructions = Column(Text, nullable=False) # , max_length=32768
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(UUID(as_uuid=True), ForeignKey('users.user_id'), nullable=False)
    
    user = relationship('User', foreign_keys=[created_by])
    
