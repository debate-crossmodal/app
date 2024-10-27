import unittest
from app import app

class ApiTestCase(unittest.TestCase):

    def setUp(self):
        """Configura o ambiente de teste antes de cada teste."""
        self.app = app.test_client()
        self.app.testing = True

    def test_vote_api(self):
        """Testa a API de submissão de votos."""
        response = self.app.post('/api/votar', json={'voto': 'candidato1'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Seu voto foi enviado com sucesso!', response.data)

    def test_vote_api_invalid(self):
        """Testa a API de submissão de votos com dados inválidos."""
        response = self.app.post('/api/votar', json={'voto': ''})  # Voto vazio
        self.assertEqual(response.status_code, 400)  # Espera erro de validação

    def test_results_api(self):
        """Testa a API de recuperação de resultados."""
        response = self.app.get('/api/resultados')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)  # Espera uma lista como resposta

if __name__ == '__main__':
    unittest.main()