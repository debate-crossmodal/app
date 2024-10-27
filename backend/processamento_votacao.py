import pandas as pd
import gspread
from google.auth import default
from google.colab import auth
from flask import jsonify

# Autenticação no Google
auth.authenticate_user()
creds, _ = default()
gc = gspread.authorize(creds)

# Abrir a planilha de votos (substitua pela URL da sua planilha)
url_votos = 'https://docs.google.com/spreadsheets/d/1GwjKAuE2RuCsNqjmfSZ5aOTmHYLRjlCwHlE0FeVcpRI/edit?resourcekey=&gid=1314903386#gid=1314903386'
planilha_votos = gc.open_by_url(url_votos)
aba_votos = planilha_votos.sheet1

# Função para processar os votos
def calcular_stv(votos):
    # Aqui você deve implementar a lógica do STV para calcular os resultados.
    # Este é um placeholder para a lógica de contagem dos votos.
    resultados = {}
    
    # Processar cada voto
    for voto in votos:
        for candidato in voto:
            if candidato not in resultados:
                resultados[candidato] = 0
            resultados[candidato] += 1
    
    return resultados

# Função para recuperar os votos da planilha
def recuperar_votos():
    # Ler os dados da planilha
    dados = aba_votos.get_all_records()
    votos = []
    
    for linha in dados:
        # Supondo que os votos estão nas colunas a partir da segunda coluna
        voto = [linha[col] for col in linha if col != 'Email do Votante']
        votos.append(voto)
    
    return votos

# Função principal para processamento dos votos
def processar_votacao():
    votos = recuperar_votos()  # Recuperar os votos da planilha
    resultados = calcular_stv(votos)  # Calcular os resultados
    return jsonify(resultados)  # Retornar os resultados como JSON

if __name__ == '__main__':
    processar_votacao()