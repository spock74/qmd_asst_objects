# -*- coding: utf-8 -*-
"""
Nome do Arquivo: uso_tokens_schema.py
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


from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession

from core.configs import settings


engine: AsyncEngine = create_async_engine(settings.DB_URL)

Session: AsyncSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)

