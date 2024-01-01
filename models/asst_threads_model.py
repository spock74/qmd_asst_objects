    from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import JSON
from core.configs import settings

class AssistantThreadModel(settings.DBBaseModel):
    __tablename__ = 'assistants_threads'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    thread_id = Column(String, primary_key=True, unique=True, nullable=False, index=True)
    object = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    metadata_ = Column(JSON)