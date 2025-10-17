import pandas as pd
import matplotlib.pyplot as plt

#Exercicio 2
# === 1. Criar DataFrame com os dados dos alunos ===
dados = pd.DataFrame({
    "Nome": ["Ana", "Bruno", "Carla", "Daniel", "Eduardo"],
    "Curso": ["Engenharia", "Computação", "Elétrica", "Computação", "Engenharia"],
    "Nota1": [8.0, 6.5, 9.0, 5.5, 7.0],
    "Nota2": [7.5, 7.0, 8.5, 6.0, 7.5],
    "Nota3": [9.0, 7.5, 9.5, 7.0, 8.0]
})

# === 2. Criar coluna "Média Geral" ===
dados["Média Geral"] = dados[["Nota1", "Nota2", "Nota3"]].mean(axis=1)
print("=== Alunos com Média Geral ===")
print(dados)

# === 3. Listar alunos com média > 8 ===
alunos_acima_8 = dados[dados["Média Geral"] > 8]
print("\n=== Alunos com média maior que 8 ===")
print(alunos_acima_8[["Nome", "Curso", "Média Geral"]])

# === 4. Média geral por curso ===
media_por_curso = dados.groupby("Curso")["Média Geral"].mean()
curso_melhor_desempenho = media_por_curso.idxmax()
print("\n=== Média Geral por Curso ===")
print(media_por_curso)
print(f"\nCurso com melhor desempenho: {curso_melhor_desempenho}")

# === 5. Gráfico de barras da média por curso ===
media_por_curso.plot(kind="bar", color="lightgreen", edgecolor="black")
plt.title("Média Geral por Curso")
plt.xlabel("Curso")
plt.ylabel("Média Geral")
plt.ylim(0, 10)
plt.tight_layout()
plt.show()