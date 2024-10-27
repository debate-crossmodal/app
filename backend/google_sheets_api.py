import gspread
from google.auth import default

def authenticate_google_sheets():
    """Autentica e retorna uma instância da API do Google Sheets."""
    creds, _ = default()  # Autentica usando as credenciais padrão
    gc = gspread.authorize(creds)
    return gc

def get_worksheet(sheet_url, worksheet_name):
    """Retorna a planilha especificada pelo URL e nome da aba."""
    gc = authenticate_google_sheets()
    sheet = gc.open_by_url(sheet_url)
    return sheet.worksheet(worksheet_name)

def read_data(sheet_url, worksheet_name):
    """Lê dados de uma planilha específica e retorna como uma lista de listas."""
    worksheet = get_worksheet(sheet_url, worksheet_name)
    return worksheet.get_all_values()

def write_data(sheet_url, worksheet_name, data):
    """Escreve dados na planilha específica."""
    worksheet = get_worksheet(sheet_url, worksheet_name)
    worksheet.append_rows(data)  # Adiciona dados ao final da planilha