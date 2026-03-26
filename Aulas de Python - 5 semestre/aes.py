print("Bem-vindo a atvidade de AES\n")
print("1. Codificar")
print("2. Decodificar")
print("3. Sair")

while True:
    opcao = int(input("\nInsira uma opção: "))

    match opcao:
        case 1:
            msg = input("Digite a mensagem: ")
            print(msg)
        case 2:
            chave = input("Digite a chave: ")
            print(chave)
        case 3:
            print("Encerrando programa...")
        case _:
            print("Opção inválida. Digite novamente.")
    if opcao == 3:
        break
    
print("Fim do programa.")
