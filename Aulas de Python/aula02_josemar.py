import csv
'''with open('arquivo.txt', 'r') as arq:
    conteudo = arq.read()
    print(conteudo)

with open('arquivo.txt', 'r') as arq:
    for linha in arq:
        print(linha.strip())'''

'''#Ler um arquivo de texto e contar quantas palavras ele possui
with open("arquivo.txt", "r") as arq:
    conteudo = arq.read()

palavras = conteudo.split() # separa pelo espaço
print("Quantidade de palavras: ", len(palavras))'''

'''#Programa que copia o conteúdo de arquivo para outro
with open("arquivo.txt", "r") as arq_origem:
    conteudo = arq_origem.read()

with open("copia.txt", "w") as arq_destino:
    arq_destino.write(conteudo)

print("Arquivo copiado com sucesso!")   '''

'''vogais = "AEIOUaeiou"
with open ("texto.txt", "r") as arq:
    for linha in arq:
        if linha and linha[0] in vogais:
            print(linha.strip())'''

#1) Crie um programa que leia números digitados pelo usuário e grave em um arquivo.

'''leitura = input('Digite alguma coisa: ')
with open('arquivo.txt', 'w') as arq:
    arq.write(leitura)'''

    
#2) Leia um CSV simples (ex.: nome, idade) e mostre em formato de tabela.

with open("listas.txt", "r") as arq:
    conteudo = arq.read()

print(conteudo)
    

#3) Leia um arquivo com diversos nomes de animais, peça pro usuário digitar um animal e verifique se existe no mesmo arquivo.


    
#4) Peça ao usuário para digitar o nome de 5 alunos. Grave esses nomes em um arquivo chamado alunos.txt (um nome por linha). Depois, reabra o arquivo e mostre na
#tela a lista de alunos cadastrados.
#5) Leia de um arquivo chamado notas.txt as notas dos alunos (uma nota por linha). Calcule a média geral da turma. Mostre a média na tela.

