# test_sistemacadastro.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import unittest
from classes.pessoa import Pessoa
from classes.sistemacadastro import SistemaCadastro

class TestSistemaCadastro(unittest.TestCase):
    def test_cadastrar_pessoa(self):
        sistema = SistemaCadastro()
        sistema.logged_in = True
        sistema.cadastrar_pessoa(nome="Jose", idade=30, peso=65, altura=1.70)
        self.assertIsNotNone(sistema.pessoas)
    
    def test_calculo_imc(self):
        pessoa = Pessoa(nome="Test-1", idade=25, peso=70, altura=1.75)
        self.assertAlmostEqual(pessoa.imc, 22.86, places=2)

    def test_alerta_imc_alto(self):
        pessoa = Pessoa(nome="Test-2", idade=25, peso=90, altura=1.75)
        self.assertTrue(pessoa.alerta_gerado)

    def test_alerta_imc_baixo(self):
        pessoa = Pessoa(nome="Test-3", idade=25, peso=50, altura=1.75)
        self.assertTrue(pessoa.alerta_gerado)

    def test_alerta_imc_normal(self):
        pessoa = Pessoa(nome="Test-4", idade=25, peso=68, altura=1.75)
        self.assertFalse(pessoa.alerta_gerado)

    def test_login_sucesso(self):
        sistema = SistemaCadastro()
        sistema.login("admin", "1234")
        self.assertTrue(sistema.logged_in)

    def test_login_falha(self):
        sistema = SistemaCadastro()
        sistema.login("admin", "wrongpass")
        self.assertFalse(sistema.logged_in)
    
    def test_listar_pessoas(self):
        sistema = SistemaCadastro()
        sistema.logged_in = True
        sistema.cadastrar_pessoa(nome="Test-1", idade=25, peso=70, altura=1.75)
        sistema.cadastrar_pessoa(nome="Test-2", idade=30, peso=75, altura=1.65)
        sistema.cadastrar_pessoa(nome="Test-3", idade=20, peso=60, altura=1.85)
        resultado = sistema.pessoas
        # teste se lista foi criada
        self.assertIsInstance(resultado, list)
        # teste se os objetos criados realmente estao na lista
        self.assertIsInstance(resultado[0], Pessoa)
        self.assertIsInstance(resultado[1], Pessoa)
        self.assertIsInstance(resultado[2], Pessoa)
        # teste se os bjetos da lista são iguais do cadastro
        self.assertEqual(resultado[0].nome, "Test-1")
        self.assertEqual(resultado[1].nome, "Test-2")
        self.assertEqual(resultado[2].nome, "Test-3")

if __name__ == "__main__":
    unittest.main()
