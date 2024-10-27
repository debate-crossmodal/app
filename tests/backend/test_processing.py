import unittest
from unittest.mock import patch, MagicMock
from processamento_votacao import calcular_stv, recuperar_votos, processar_votacao

class TestProcessamentoVotacao(unittest.TestCase):

    @patch('processamento_votacao.aba_votos.get_all_records')
    def test_recuperar_votos(self, mock_get_all_records):
        """Teste para verificar se a função recupera os votos corretamente."""
        mock_get_all_records.return_value = [
            {'Email do Votante': 'usuario1@gmail.com', 'Candidato 1': 'Candidato A', 'Candidato 2': 'Candidato B'},
            {'Email do Votante': 'usuario2@gmail.com', 'Candidato 1': 'Candidato B', 'Candidato 2': 'Candidato A'}
        ]
        
        votos = recuperar_votos()
        
        # Verifica se os votos foram recuperados corretamente
        self.assertEqual(len(votos), 2)
        self.assertEqual(votos[0], ['Candidato A', 'Candidato B'])
        self.assertEqual(votos[1], ['Candidato B', 'Candidato A'])
    
    def test_calcular_stv(self):
        """Teste para verificar se a função calcula os resultados corretamente."""
        votos = [
            ['Candidato A', 'Candidato B'],
            ['Candidato B', 'Candidato A'],
            ['Candidato A', 'Candidato C'],
            ['Candidato C', 'Candidato A']
        ]
        
        resultados = calcular_stv(votos)
        
        # Verifica se os resultados estão corretos
        self.assertEqual(resultados['Candidato A'], 3)
        self.assertEqual(resultados['Candidato B'], 2)
        self.assertEqual(resultados['Candidato C'], 1)

    @patch('processamento_votacao.recuperar_votos')
    @patch('processamento_votacao.calcular_stv')
    def test_processar_votacao(self, mock_calcular_stv, mock_recuperar_votos):
        """Teste para verificar se a função processar_votacao retorna os resultados corretamente."""
        mock_recuperar_votos.return_value = [['Candidato A', 'Candidato B']]
        mock_calcular_stv.return_value = {'Candidato A': 1, 'Candidato B': 0}
        
        resultados = processar_votacao()
        
        # Verifica se os resultados estão corretos
        self.assertEqual(resultados.json, {'Candidato A': 1, 'Candidato B': 0})

if __name__ == '__main__':
    unittest.main()