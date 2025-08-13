l = [1, 2, 3, 4, 5]
l.append(6)
l.insert(1, 10)
print (l)
print (l[1])
l.pop(1)
print (l)
l.remove(1)
print (l)
l.reverse()
print (l)
l.clear()
print (l)
l2 = ['Rebeca', 'João', 'Matheus', 'Arthur']
print (l2)
l2.sort()
print (l2)
a = [3, 4, 5, 10]
soma1 = list()

for i in a:
    soma1 += [i+1]

print (soma1)

b = [0, 4, 5 ,6 ,7, 9, 10, 100]
n = list()
for i in a:
    if i%2 == 0:
        n+=[i*i]

print (n)        
x = [1,2,3,4,5,6,7,8,9]
print (x[0:7:2])

y = (1, 2, 4)
z = (4, 0, 0)
print (z + y)

list = {'idade':21, 'nome':'João', 'cidade':'Curitiba'}
print (list['idade'])

#Exercicio 1 - Crie um Python Script que conte quantas vezes cada nome está presente em uma lista
#e armazena essa contagem em um dicionário

lista = ['Carlos', 'Gustavo', 'Luiz', 'Hadassa', 'Vinicius', 'Gustavo', 'Pedro', 'Carlos']
dicionario = {}
for i in lista:
    print (lista.count(i))
    dicionario[nome] = lista.count(i)
