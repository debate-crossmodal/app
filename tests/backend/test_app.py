import unittest
from app import app
from google_sheets_api import write_data, read_data

class AppTestCase(unittest.TestCase):

    def setUp(self):
        """Configura o ambiente de teste antes de cada teste."""
        self.app = app.test_client()
        self.app.testing = True

    def test_vote_submission(self):
        """Testa a submissão de votos."""
        response = self.app.post('/api/votar', json={'voto': 'candidato1'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Seu voto foi enviado com sucesso!', response.data)

    def test_read_votes(self):
        """Testa a leitura de votos da planilha."""
        data = read_data('link_para_votos', 'Votos')
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)  # Verifica se há dados

    def test_write_results(self):
        """Testa a escrita de resultados na planilha."""
        test_results = [['candidato1', 5], ['candidato2', 3]]
        write_data('link_para_resultados', 'Resultados', test_results)
        results = read_data('link_para_resultados', 'Resultados')
        self.assertIn(['candidato1', '5'], results)  # Verifica se os resultados foram escritos

if __name__ == '__main__':
    unittest.main()