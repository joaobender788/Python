import pandas as pd
import matplotlib.pyplot as plt

#Exercicio 3
alunos = pd.read_csv("alunos.csv")
notas = pd.read_csv("notas.csv")

dados_completos = pd.merge(alunos, notas, on="Matricula")

media = dados_completos.groupby("Curso")["Notas"].mean()
acima_de_8 = dados_completos[dados_completos["Notas"]>=8]

plt.bar(media.index, media.values)
plt.title("Média de Notas por Curso")
plt.xlabel("Curso")
plt.ylabel("Média das Notas")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

print(media)
print(acima_de_8)
