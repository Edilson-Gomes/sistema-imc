# test_sistemacadastro.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import unittest
from classes.pessoa import Pessoa
from classes.sistemacadastro import SistemaCadastro

class TestSistemaCadastro(unittest.TestCase):
    def test_calculo_imc(self):
        pessoa = Pessoa(nome="Test-1", idade=25, peso=70, altura=1.75)
        self.assertAlmostEqual(pessoa.imc, 22.86, places=2)
        #print(f'Testado! \n')

    def test_alerta_imc_alto(self):
        pessoa = Pessoa(nome="Test-2", idade=25, peso=90, altura=1.75)
        self.assertTrue(pessoa.alerta_gerado)
        #print(f'Testado! \n')


    def test_alerta_imc_baixo(self):
        pessoa = Pessoa(nome="Test-3", idade=25, peso=50, altura=1.75)
        self.assertTrue(pessoa.alerta_gerado)
        #print(f'Testado! \n')

    def test_alerta_imc_normal(self):
        pessoa = Pessoa(nome="Test-4", idade=25, peso=68, altura=1.75)
        self.assertFalse(pessoa.alerta_gerado)
        #print(f'Testado! \n')

    def test_login_sucesso(self):
        sistema = SistemaCadastro()
        sistema.login("admin", "1234")
        self.assertTrue(sistema.logged_in)

    def test_login_falha(self):
        sistema = SistemaCadastro()
        sistema.login("admin", "wrongpass")
        self.assertFalse(sistema.logged_in)

if __name__ == "__main__":
    unittest.main()
