import unittest
from unittest.mock import MagicMock
import logging
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controller import Controller
from view import View

logging.basicConfig(level=logging.INFO)

class TestView(unittest.TestCase):
    def setUp(self):
        print("Iniciando teste para a classe View")
        self.controller = Controller()
        self.view = View(self.controller)
        self.controller.model.buscar_dados = MagicMock(return_value=([100, 200, 300], ['2022-05-01', '2022-05-02', '2022-05-03']))

    def test_buscar_dados(self):
        
        self.view.ativo_selecionado.set("AAPL")
        self.view.periodo_selecionado.set("5d")
        self.view.buscar_dados()
        self.assertEqual(self.view.ax.get_title(), "Gráfico do Preço do AAPL (5d)")
        self.assertEqual(self.view.ax.get_xlabel(), "Data")
        self.assertEqual(self.view.ax.get_ylabel(), "Preço")
        self.assertEqual(self.view.ax.lines[0].get_xydata().tolist(), [[737998.0, 100.0], [737999.0, 200.0], [738000.0, 300.0]])
        print("Teste para verificar se o gráfico é gerado corretamente com os dados buscados")
        
if __name__ == '__main__':
    unittest.main()
