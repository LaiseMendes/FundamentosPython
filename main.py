from cadastro import Cadastro
from queries import Query

print("1. Cadastrar?\n2. Fazer uma query? ")
opcao = input("digite opção desejada: ")

if opcao == "1":
    Cadastro().armazena()
elif opcao == "2":
    Query().busca()