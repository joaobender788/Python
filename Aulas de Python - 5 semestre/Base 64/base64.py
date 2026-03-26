#Base64 - Atividade 1
import base64

print("Bem-vindo\n")
print("1- Codificar")
print("2- Decodificar")
print("3- Sair\n")
opcao = int(input("Escolha uma opcao: "))

match opcao:
    case 1:
        msg = input("Digite o que deseja codificar: ")
        msgbytes = msg.encode('utf-8')
        msgdbytes = base64.b64encode(msgbytes)
        msgd = msgdbytes.decode('utf-8')
        print("Senha codificada: " + msgd)
    case 2:
        msg2 = input("Digite o que você quer decodificar: ")
        msgbytes = msg2.encode('utf8')
        msgdbytes2 = base64.b64decode(msgbytes)
        msgd2 = msgdbytes2.decode('utf-8')
        print("Senha decodificada: " + msgd2)
    case 3:
        print("Saindo...")
    case _:
        print("Opção inválida.")

print("Fim do programa.")
