# main.py
from classes.sistemacadastro import SistemaCadastro

def main():
    sistema = SistemaCadastro()

    # Realizando login ("admin", "1234")
    sistema.login("admin", "1234")

    # Cadastrando pessoas
    sistema.cadastrar_pessoa(nome="Joao", idade=30, peso=85, altura=1.80)
    sistema.cadastrar_pessoa(nome="Maria", idade=28, peso=50, altura=1.60)

    # Listando pessoas cadastradas
    sistema.listar_pessoas()

if __name__ == "__main__":
    main()
