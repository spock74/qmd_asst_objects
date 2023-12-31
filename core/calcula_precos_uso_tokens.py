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

import pandas as pd

def calcular_preco(modelo, tokens_entrada, tokens_saida):
    """
    Calcula o preço total para um determinado modelo baseado no número de tokens de entrada e saída.

    Parâmetros:
    modelo (str): O nome do modelo para o qual calcular o preço.
    tokens_entrada (int): O número de tokens de entrada.
    tokens_saida (int): O número de tokens de saída.

    Retorna:
    preco_total (float): O preço total calculado.
    """
    
    # Leia o arquivo CSV
    df = pd.read_csv('precos.txt')

    # Encontre a linha que corresponde ao modelo
    linha = df.loc[df['model'] == modelo]

    # Obtenha os preços de entrada e saída
    preco_entrada = linha['preco_input_1000'].values[0]
    preco_saida = linha['preco_output_1000'].values[0]

    # Calcule o preço total
    preco_total = (tokens_entrada * preco_entrada/1000) + (tokens_saida * preco_saida/1000)

    return preco_total

# Exemplo de uso:
if __name__ == '__main__':
    
    preco_total = calcular_preco('gpt-4', 1000, 1000)
    print(f'Preço total: {preco_total}')