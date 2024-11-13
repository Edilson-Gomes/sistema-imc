# pessoa.py

class Pessoa:
    def __init__(self, nome, idade, peso, altura, email=None, telefone=None):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.email = email
        self.telefone = telefone
        self.imc = self.calcular_imc()
        self.alerta_gerado = self.verificar_alerta()

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    def verificar_alerta(self):
        # Faixa de IMC saudável, segundo a OMS
        if self.imc < 18.5 or self.imc > 24.9:
            return True
        return False
