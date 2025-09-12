import random
#Exercicio 2
numero = random.randint(1, 100)

guess = (int(input("Começando novo jogo! Digite um número de 1 a 100: ")))

while guess != numero:
  if guess > numero:
      print (f"Número é menor que {guess}")
      guess = int(input("Tente novamente: "))
  elif guess < numero:
      print (f"Número maior que {guess}")  
      guess = int(input("Tente novamente: "))

print(f"Parabéns! o número é igual a {guess}")

#Exercicio 4
#print("Bem-vindo ao banco! Escolha uma das opções: ")
#escolha = 0
#saldo = 0
#
#while escolha != 4:
#    print("\n1- Depositar\n2- Sacar\n3- Ver saldo\n4- Sair")
#    escolha = int(input("Escolha: "))
#
#    match escolha:
#        case 1:
#            deposito = float(input("Digite o quanto quer depositar: "))
#            saldo += deposito
#        case 2:
#            saque = float(input("Digite o quanto quer sacar: "))
#            saldo -= saque
#        case 3:
#            print(f"Saldo: {saldo}")  
#        case 4:
#            print("Encerrando programa...")    
#        case _:
#            print("Opção invalida.") 
#
#print("Programa encerrado.")            

#Exercicio 8
#
#numero = int(input("Digite um número para ver sua tabuada do 1 ao 10: "))
#
#for i in range (1, 11):
#    print (f"{numero} x {i} = ", numero * i)

#Exercicio 9
#print("Digite números para calcular a média. Digite 'fim' para encerrar.")
#soma = 0
#quantidade = 0
#
#while True:
#    entrada = input("Digite um número (ou 'fim'): ")
#
#    if entrada.lower() == "fim":
#
#    try:
#        numero = float(entrada)
#        soma += numero
#        quantidade += 1
#    except ValueError:
#        print("Entrada inválida. Por favor, digite um número ou 'fim'.")
#
#if quantidade > 0:
#    media = soma / quantidade
#    print(f"Média dos {quantidade} números digitados: {media:.2f}")
#else:
#    print("Nenhum número válido foi digitado.")

#Exercicio 10
#    
#nome = (input("Digite seu nome: "))
#nota1 = float(input("Digite a nota 1: "))        
#nota2 = float(input("Digite a nota 2: "))
#nota3 = float(input("Digite a nota 3: "))
#
#media = (nota1 + nota2 + nota3)/3
#
#print(f"Nome: {nome}")
#
#if media >= 7:
#    print("Situação: Aprovado.")
#elif media >= 5 and media < 7:
#    print("Situação: Recuperação.")
#else:
#    print("Situação: Reprovado.")    
