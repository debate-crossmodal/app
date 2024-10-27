import os

# Configurações do Google Sheets
GOOGLE_SHEETS_VOTOS_URL = os.getenv('GOOGLE_SHEETS_VOTOS_URL', 'link_para_votos')
GOOGLE_SHEETS_RESULTADOS_URL = os.getenv('GOOGLE_SHEETS_RESULTADOS_URL', 'link_para_resultados')

# Configurações de autenticação
GOOGLE_API_CREDENTIALS = os.getenv('GOOGLE_API_CREDENTIALS', 'caminho_para_credenciais.json')

# Outras configurações
DEBUG = True  # Mude para False em produção