import pandas as pd
from google_sheets_api import read_data

def load_votes(sheet_url):
    """Carrega os votos da planilha e retorna como um DataFrame."""
    data = read_data(sheet_url, 'Votos')  # Nome da aba onde os votos estão armazenados
    df = pd.DataFrame(data[1:], columns=data[0])  # Usando a primeira linha como cabeçalho
    return df

def calculate_results(votes_df):
    """Calcula os resultados da votação a partir do DataFrame de votos."""
    # Exemplo de cálculo simples: contagem de votos
    results = votes_df['candidato'].value_counts().reset_index()
    results.columns = ['candidato', 'total_votos']
    return results

def save_results(sheet_url, results_df):
    """Salva os resultados calculados de volta na planilha de resultados."""
    from google_sheets_api import write_data
    results_data = results_df.values.tolist()
    write_data(sheet_url, 'Resultados', results_data)  # Especifica a aba de resultados