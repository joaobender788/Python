import pandas as pd
import matplotlib.pyplot as plt

# Lê o arquivo CSV
dados = pd.read_csv("alunos_notas.csv")

# Verifica se as colunas necessárias existem
if not set(["Nome", "Curso", "Nota"]).issubset(dados.columns):
    raise ValueError("O arquivo CSV deve conter as colunas: Nome, Curso, Nota")

# Converte a coluna 'Nota' para numérico (caso tenha sido lida como texto)
dados["Nota"] = pd.to_numeric(dados["Nota"], errors="coerce")

# Remove linhas com nota inválida ou ausente
dados = dados.dropna(subset=["Nota"])

# Maior e menor nota por curso
estatisticas_curso = dados.groupby("Curso")["Nota"].agg(["max", "min"]).reset_index()
estatisticas_curso.rename(columns={"max": "Maior Nota", "min": "Menor Nota"}, inplace=True)

# Média geral
media_geral = dados["Nota"].mean()

# Alunos com nota acima da média
alunos_acima_media = dados[dados["Nota"] > media_geral]
qtd_acima_media = len(alunos_acima_media)

# Gráfico de pizza: proporção de alunos por curso
alunos_por_curso = dados["Curso"].value_counts()
alunos_por_curso.plot.pie(autopct="%1.1f%%", startangle=90)
plt.title("Proporção de Alunos por Curso")
plt.ylabel("")  # Oculta o rótulo do eixo Y
plt.tight_layout()
plt.show()

# Mostrar resultados no console
print("\n=== Maior e Menor Nota por Curso ===")
print(estatisticas_curso)

print(f"\nMédia geral das notas: {media_geral:.2f}")
print(f"Quantidade de alunos com nota acima da média: {qtd_acima_media}")

# Gravar resultados em relatorio.csv
relatorio = estatisticas_curso.copy()
relatorio["Média Geral"] = media_geral
relatorio["Alunos Acima da Média"] = qtd_acima_media

# Como isso é por curso, adicionamos os valores apenas na primeira linha para evitar repetição
relatorio.loc[1:, ["Média Geral", "Alunos Acima da Média"]] = ""

relatorio.to_csv("relatorio.csv", index=False, encoding="utf-8")

print("\nRelatório salvo como relatorio.csv.")
