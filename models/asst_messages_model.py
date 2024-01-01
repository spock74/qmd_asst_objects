from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship
from core.configs import settings

class AssistantMessageModel(settings.DBBaseModel):
    __tablename__ = 'assistants_messages'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    message_id = Column(String, nullable=False, unique=True, index=True,primary_key=True)    
    object = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    thread_id = Column(String, nullable=False, index=True)
    role = Column(String)
    content = Column(JSON)
    file_ids = Column(JSON)
    assistant_id = Column(String, ForeignKey('assistants.assistant_id'))
    run_id = Column(String)
    metadata_ = Column(JSON)

    assistant = relationship("AssistantModel", back_populates="assistants_messages")