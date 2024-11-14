# main.py
from classes.sistemacadastro import SistemaCadastro
from classes.pessoa import Pessoa

sistema = SistemaCadastro()
acesso = True

print(f"{' BEM-VINDO AO SISTEMA IMC ':#^40}")
print(f"{'Faça o login para começar.':-^40}")
while(acesso):
    sistema.login(input("Login: "), input(f"Senha: "))
    while sistema.logged_in:
        print(f"{'SISTEMA IMC':-^40}")
        print(f"{'1-cadastrar | 2-lista | 3-IMC | 4-Logout':=^40}")
        num = input(f"{'Escolha uma opção: ':-^40}")
        match num:
            case '1':
                sistema.cadastrar_pessoa(input(f'Nome: '), int(input(f'Idade: ')), float(input(f'Peso(kg): ')), float(input(f'Altura(m): ')))
            case '2':
                print(f"\n{'Cadastrados':-^40}")
                sistema.listar_pessoas()
                print(f"\n")
            case '3':
                sistema.imc(float(input(f'Peso(kg): ')), float(input(f'Altura(m): ')))
            case '4':
                sistema.logged_in = False    
                print(f"Logout com sucesso! ")
                acesso = False
            case _:
                print(f"{'Opçaõ inválida!':-^40}")
            
print(f"{'Sistema finalizado!':-^40}")


