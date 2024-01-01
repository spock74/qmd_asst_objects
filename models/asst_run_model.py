
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import  relationship
from sqlalchemy.sql import func
import uuid
from sqlalchemy.dialects.postgresql import UUID
from core.configs import settings



class AssistantRunModel(settings):
    __tablename__ = "assistants_runs"

    run_id = Column(String, primary_key=True, nullable=False) 
    object = Column(String(255), nullable=False)
    assistant_id = Column(String, ForeignKey('assistants.assistant_id'))
    thread_id = Column(String, ForeignKey('assistants_threads.thread_id'))
    model = Column(String, nullable=False)
    instructions = Column(String, nullable=False)
    tools = Column(JSON, nullable=False)
    file_ids = Column(JSON, nullable=True)
    metadata_ = Column(JSON, nullable=False)
    run_started_by = 


    status = 
    started_at = 
    expires_at = 
    cancelled_at = 
    failed_at = 
    completed_at = 
    last_error = 



    checked_at = 
    checked_status = 
                                      


    id = 
    custom_uuid = 
    created_by = 
    created_at = 
