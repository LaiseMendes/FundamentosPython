array = []
while True:
    print("1. Cadastrar seu nome\n 2. Consultar seu nome \n")
    opcao = input("digite a opção desejada:")
    if opcao == "1":
        item = input("Digite um item:")
        array.append(item)
        print(array)
    elif opcao == "2":
        for dado in array:
            print(dado)
    continuar = input("Continuar?")
    if continuar != 'sim':
        break 
