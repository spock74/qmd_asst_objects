
# -*- coding: utf-8 -*-
"""
Nome do Arquivo: configs.py
Autor: Jose E Moraes
Empresa proprietária: QMD-QUERO MEUS DIREITOS
Copyright: 2023

Todos os direitos reservados. Nenhuma parte deste código pode ser reproduzida, distribuída, 
ou transmitida de qualquer forma ou por qualquer meio, incluindo fotocópia, gravação ou 
outros métodos eletrônicos ou mecânicos, sem a permissão prévia por escrito do proprietário 
do copyright e da empresa proprietária exceto no caso de breves citações incorporadas em revisões críticas e certos 
outros usos não comerciais permitidos pela lei de direitos autorais.

Para solicitações de permissão, escreva para a empresa QMD-QUERO MEU DIREITOS, 
endereço fornecido abaixo.

AVISO: Este código é fornecido 'como está' e qualquer expressa ou implícita garantias, 
incluindo, mas não limitado a, as garantias implícitas de comercialização e adequação a 
um propósito específico são renunciadas. Em nenhum caso o autor ou detentores de direitos 
autorais serão responsáveis por qualquer reivindicação, danos ou outra responsabilidade, 
seja em uma ação de contrato, delito ou de outra forma, decorrente de, fora de ou em 
conexão com o software ou o uso ou outras negociações no software.
"""


from typing import List
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from typing import ClassVar

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    # CONNECTION_STRING_EMBEDDING: str = 'postgresql+asyncpg://geek:university@localhost:5432/faculdade'
    DB_URL: str = "postgresql+asyncpg://postgres:@localhost:5432/jose_testes"
    DBBaseModel: ClassVar = declarative_base()
    #--------------------------------------------------------------------------------------
    ## TODO anotacoes de tipo nas abelas de embedding
    CONNECTION_STRING_EMBEDDING: str = 'postgresql+psycopg2://postgres:@localhost:5432/qmd02'
    #--------------------------------------------------------------------------------------
    _SERVER_ = 'http://localhost:8001/api/v1'
    TEMPO_INVALIDAR_CACHE_DESPACHOS_MINUTOS: int = 60 * 60
    NOME_TEMP_FILE: str = './digestao_temp.txt'
    NOME_TEMP_CACHE_FILE: str = './digestao_temp.txt'
    OPENAI_API_KEY_ENV_NAME: str = "OPENAI_QMD_API_KEY"
    OPENAI_API_KEY_ENV_NAME: str = "OPENAI_ZEH_API_KEY"
    OPENAI_API_GPT_4_MODEL_NAME: str = 'gpt-4'
    OPENAI_API_GPT_4_1106_MODEL_NAME: str = 'gpt-4-1106-preview'
    OPENAI_API_GPT_3_5_TUBO_MODEL_NAME: str = 'gpt-3.5-turbo'
    OPENAI_API_GPT_3_5_1106_MODEL_NAME: str = 'gpt-3.5-turbo-1106'
    OPENAI_API_GPT_3_5_16_K_MODEL_NAME: str = 'gpt-3.5-turbo-16k'

    



        
settings: Settings = Settings()