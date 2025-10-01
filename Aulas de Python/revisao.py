import math

'''Ler dois valores emostrar a soma
num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))
num3 = num1 + num2
print(num3)

#Calcular a distância entre dois pontos
x1 = int(input('Digite o X do primeiro ponto: '))
y1 = int(input('Digite o Y do primeiro ponto: '))
x2 = int(input('Digite o X do segundo ponto: '))
y2 = int(input('Digite o Y do segundo ponto: '))
d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(d)'''

'''#Ler 3 medidas de um triângulo, verificar se realmente essas medidas formar um triângulo,
#e se formarem, dizer qual triângulo foi formado
lado1 = int(input('Informe o primeiro lado: '))
lado2 = int(input('Informe o segundo lado: '))
lado3 = int(input('Informe o terceiro lado: '))

ab = lado1 + lado2
bc = lado2 + lado3
ac = lado1 + lado3

if ab > lado3 and ac > lado2 and bc > lado1:
    print('O triângulo é válido.')
else:
    print('O triângulo é inválido.')

if lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print('Triângulo escaleno')
elif lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
    print('Triângulo equilátero')
else:
    print('Triângulo isósceles')'''

#Formatos de FOR

# de 0 até 4
for i in range (5):
    print(i)

# de 2 até 6
for i in range (2,7):
    print (i)

# de 10 até 0, de -2 em -2
for iin range(10, -1, -2):
    print(i)

# percorrendo listas
frutas = ['maçã', 'banana', 'uva']
for i in frutas:
    print (i)

# percorrendo strings
for letra in 'Python':
    print(letra)
    
# percorrendo tuplas
numeros = (10, 20, 30)
for i in numeros:
    print (i)

# percorrendo dicionários
pessoa = ('nome':'Lambarildo', 'idade':23, 'cidade': 'Recife')

for i in pessoa:
    print (i)
for i, j in pessoa.items() ;
    print (i, "->", j)

# for com enumerate()
nomes = ['Ano', 'Bruno', 'Carlos']
for i , nome in enumerate(nomes):
    print(i, nome)

# for com zip() Percorre duas (ou mais) listas ao mesmo tempo
alunos = ['Ana', 'Bruno', 'Carlos']
notas = [8, 9, 7]
for aluno, nota in zip(alunos, notas):
    print(aluno, "tirou", nota)

# Criando listas (vetores)
# Vetor vazio
vetor = []
# Vetor com valores
vetor = [10, 20, 30, 40]
# Adicionais e removendo
vetor.append(50) #Adiciona ao fim
vetor,insert(2, 15) #Insere na posição 2
vetor.pop() #remove último elemento
vetor.remove (20) #Removeo valor 20

#Criando uma matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

#Percorrendo a matriz
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()
