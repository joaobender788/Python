import hashlib
import os

def preparar_cifragem(senha):
    salt = os.urandom(16)
    chave = hashlib.pbkdf2_hmac(
    'sha256',
    senha.encode(),
    salt,
    10000
    )
    iv = os.urandom(16)

    return salt, chave, iv


print("PROGRAMA DE COFRE\n")
print("1. Cifrar um arquivo")
print("2. Decifrar um arquivo")
print("3. Testar com vetor conhecido")
print("4. Sair")
opcao = int(input("Valor: "))

match opcao:
    case 1:
        senha = input("Digite sua senha: ")
        s, c, i = preparar_cifragem(senha)

        print(f"Salt (hex): {s.hex()}")
        print(f"Chave AES (hex): {c.hex()}")
        print(f"IV (hex): {i.hex()}")
    case 2:
        print("...")
    case 3:
        print("Encerrando...")
    case _:
        print("Opção inválida.")

print("Fim de programa.")
