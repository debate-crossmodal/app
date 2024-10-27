from flask import Flask
from .auth import register_auth
from .data_processing import process_data

def create_app():
    """Cria e configura a aplicação Flask."""
    app = Flask(__name__)

    # Configurações da aplicação (pode ser carregado a partir de um arquivo de configuração)
    app.config['SECRET_KEY'] = 'sua_chave_secreta'  # Altere para uma chave secreta forte

    # Registro do blueprint de autenticação
    register_auth(app)

    # Outras configurações e rotas
    @app.route('/')
    def home():
        return "Bem-vindo ao sistema de votação!"

    return app

# Função para processar dados (chamada em outro lugar do código)
def process_votes():
    """Função que pode ser chamada para processar os votos."""
    return process_data()  # Chama a função de processamento de dados

if __name__ == '__init__':
    app = create_app()