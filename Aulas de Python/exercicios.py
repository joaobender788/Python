import random
#Exercicio 2
#numero = random.randint(1, 100)
#
#guess = (int(input("Começando novo jogo! Digite um número de 1 a 100: ")))
#
#while guess != numero:
#  if guess > numero:
#      print (f"Número é menor que {guess}")
#      guess = int(input("Tente novamente: "))
#  elif guess < numero:
#      print (f"Número maior que {guess}")  
#      guess = int(input("Tente novamente: "))

#print(f"Parabéns! o número é igual a {guess}")

#Exercicio 4
print("Bem-vindo ao banco! Escolha uma das opções: \n")
print("1- Depositar\n2- Sacar\n3- Ver saldo\n4- Sair")
escolha = (input("Escolha: "))
saldo = 0

match escolha:
    case 1:
        deposito = float(input("Digite o quanto quer depositar: "))
        saldo =+ deposito
    case 2:
        saque = float(input("Digite o quanto quer depositar: "))
        saldo =- saque
    case 3:
        print(f"Saldo: {saldo}")
        
#Exercicio 8

numero = int(input("Digite um número para ver sua tabuada do 1 ao 10: "))

for i in range (1, 10):
    print (f"{numero} x {i} = ", numero * i)

#Exercicio 10
    
nome1 = (input("Digite o nome do primeiro aluno: "))
nome2 = (input("Digite o nome do segundo aluno: "))
nome3 = (input("Digite o nome do terceiro aluno: "))   

nota1 = int(input(f"Digite a nota 1 do {nome1}"))
nota2 = int(input(f"Digite a nota 1 do {nome1}"))
nota3 = int(input(f"Digite a nota 1 do {nome1}"))         
