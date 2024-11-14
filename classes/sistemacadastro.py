# sistemacadastro.py
from classes.pessoa import Pessoa

class SistemaCadastro:
    def __init__(self):
        self.pessoas = []
        self.logged_in = False

    def login(self, username, password):
        if username == "admin" and password == "1234":
            self.logged_in = True
            print("Login bem-sucedido!")
        else:
            print("Login falhou. Usuario ou senha incorretos.")

    def cadastrar_pessoa(self, nome, idade, peso, altura, email=None, telefone=None):
        if not self.logged_in:
            print("Voce precisa estar logado para cadastrar.")
            return
        
        nova_pessoa = Pessoa(nome, idade, peso, altura, email, telefone)
        self.pessoas.append(nova_pessoa)
        print(f"Pessoa cadastrada com sucesso: {nova_pessoa.nome}")
        
        if nova_pessoa.alerta_gerado:
            print(f"Alerta: O IMC de {nova_pessoa.nome} esta fora do peso ideal.")

    def listar_pessoas(self):
        for pessoa in self.pessoas:
            print(f"Nome: {pessoa.nome}, IMC: {pessoa.imc:.2f}, Alerta: {pessoa.alerta_gerado}")
    
    def imc(self, peso, altura):
        imc = (peso / (altura ** 2))
        print(f'{imc:.2f}')
        if imc < 18.5:
            print("Atenção seu IMC esta baixo!")
        elif imc > 24.9:
            print("Atenção seu IMC esta alto!")
        else:
            print("Seu IMC está regular.")
