from sqlalchemy import create_engine
from models.__all_models import AssistantModel
from models.__all_models import UserModel

engine = create_engine("postgresql://postgres:@localhost:5432/jose_testes")

from core.configs import settings

def create_tables():
    settings.DBBaseModel.metadata.drop_all
    settings.DBBaseModel.metadata.create_all(bind=engine)   