from flask import Blueprint, redirect, url_for, session, request, jsonify
from google.oauth2 import id_token
from google.auth.transport import requests
import os

# Inicializa o blueprint para autenticação
auth_bp = Blueprint('auth', __name__)

# Configurações do cliente OAuth 2.0
GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')

@auth_bp.route('/login', methods=['POST'])
def login():
    """Rota para lidar com o login do usuário via Google."""
    token = request.json.get('token')
    
    # Verifica o token com a API do Google
    try:
        id_info = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)
        session['user_id'] = id_info['sub']  # Armazena o ID do usuário na sessão
        session['email'] = id_info['email']  # Armazena o email do usuário na sessão
        return jsonify({'status': 'success', 'email': session['email']}), 200
    except ValueError:
        return jsonify({'status': 'error', 'message': 'Token inválido'}), 400

@auth_bp.route('/logout', methods=['POST'])
def logout():
    """Rota para lidar com o logout do usuário."""
    session.pop('user_id', None)  # Remove o ID do usuário da sessão
    session.pop('email', None)  # Remove o email do usuário da sessão
    return jsonify({'status': 'success'}), 200

def is_authenticated():
    """Verifica se o usuário está autenticado."""
    return 'user_id' in session

def get_user_email():
    """Retorna o email do usuário autenticado, se disponível."""
    return session.get('email')

# Registra o blueprint na aplicação principal
def register_auth(app):
    app.register_blueprint(auth_bp)