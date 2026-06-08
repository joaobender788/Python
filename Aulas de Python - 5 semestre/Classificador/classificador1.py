import numpy as np
import pandas as pd
from collections import Counter
from pprint import pprint
from pickle import dump

from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

from imblearn.over_sampling import SMOTE

print("Iniciando o teste do classificador...")

# 1. Carregar a base de dados
try:
    dados = pd.read_csv('diabetes.csv')
    print("Base de dados 'diabetes.csv' carregada com sucesso!")
except FileNotFoundError:
    print("Erro: O arquivo 'diabetes.csv' não foi encontrado na mesma pasta do script.")
    exit()

# Separar atributos e classe
dados_atributos = dados.drop(columns=['Outcome'])
dados_classe = dados['Outcome']

# 2. Balanceamento de dados com SMOTE
resampler = SMOTE(random_state=42)
atributos_b, classes_b = resampler.fit_resample(dados_atributos, dados_classe)

print('\n#### FREQUENCIA DAS CLASSES APOS O BALANCEAMENTO ###')
print(Counter(classes_b))

# 3. Segmentação em Treino e Teste
atributos_train, atributos_teste, classe_train, classe_test = train_test_split(
    atributos_b, classes_b, test_size=0.3, random_state=42
)

# 4. Normalização (Crucial para SVM e algoritmos de distância)
scaler = StandardScaler()
atributos_train_scaled = scaler.fit_transform(atributos_train)
atributos_teste_scaled = scaler.transform(atributos_teste)

# ==========================================
# OTIMIZACAO DE HIPERPARAMETROS
# ==========================================
print("\nOtimizando hiperparametros dos modelos...")

# --- Random Forest ---
rf_grid = {
    'n_estimators': [int(x) for x in np.linspace(10, 200, 10)],
    'criterion': ['gini', 'entropy'],
    'max_depth': [None] + [int(x) for x in np.linspace(10, 50, 5)],
    'min_samples_split': [2, 5, 10],
    'max_features': ['sqrt', 'log2']
}
rf_search = RandomizedSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_distributions=rf_grid, n_iter=10, cv=3, verbose=0, n_jobs=-1, random_state=42
)
rf_search.fit(atributos_train_scaled, classe_train)
best_rf = rf_search.best_estimator_

# --- SVM ---
svm_grid = {
    'C': [0.1, 1, 10, 100],
    'gamma': ['scale', 'auto', 0.001, 0.01, 0.1, 1],
    'kernel': ['rbf', 'linear', 'sigmoid']
}
svm_search = RandomizedSearchCV(
    estimator=SVC(random_state=42),
    param_distributions=svm_grid, n_iter=10, cv=3, verbose=0, n_jobs=-1, random_state=42
)
svm_search.fit(atributos_train_scaled, classe_train)
best_svm = svm_search.best_estimator_

# --- Gradient Boosting ---
gb_grid = {
    'n_estimators': [50, 100, 150],
    'learning_rate': [0.01, 0.05, 0.1, 0.2],
    'max_depth': [3, 4, 5, 6],
    'subsample': [0.7, 0.8, 0.9, 1.0]
}
gb_search = RandomizedSearchCV(
    estimator=GradientBoostingClassifier(random_state=42),
    param_distributions=gb_grid, n_iter=10, cv=3, verbose=0, n_jobs=-1, random_state=42
)
gb_search.fit(atributos_train_scaled, classe_train)
best_gb = gb_search.best_estimator_

# ==========================================
# AVALIACAO E SELECAO AUTOMATICA PARA PRODUCAO
# ==========================================
modelos = {
    'Random Forest': best_rf,
    'SVM': best_svm,
    'Gradient Boosting': best_gb
}

resultados = {}
print('\n### RESULTADOS DETALHADOS DOS MODELOS ###\n')

for nome, modelo in modelos.items():
    pred = modelo.predict(atributos_teste_scaled)
    
    acuracia = accuracy_score(classe_test, pred)
    tn, fp, fn, tp = confusion_matrix(classe_test, pred).ravel()
    especificidade = tn / (tn + fp)
    sensibilidade = tp / (tp + fn)
    
    resultados[nome] = {
        'objeto': modelo,
        'Acuracia': acuracia,
        'Especificidade': especificidade,
        'Sensibilidade': sensibilidade
    }
    
    print(f"--- {nome} ---")
    print(f"Acuracia: {acuracia:.4f} | Sensibilidade: {sensibilidade:.4f} | Especificidade: {especificidade:.4f}\n")

# Regra de decisao automatica baseada na maior Acuracia Geral
melhor_nome = max(resultados, key=lambda k: resultados[k]['Acuracia'])
melhor_modelo_objeto = resultados[melhor_nome]['objeto']

print("="*60)
print(f"VEREDITO PARA PRODUCAO: O modelo mais adequado e o [{melhor_nome}]")
print("="*60)
print(f" Justificativa Automatica:")
print(f" - Apresentou a maior eficiencia global com {resultados[melhor_nome]['Acuracia']:.2%} de acuracia.")
print(f" - Mantem um equilibrio entre Sensibilidade ({resultados[melhor_nome]['Sensibilidade']:.2%})")
print(f"   e Especificidade ({resultados[melhor_nome]['Especificidade']:.2%}).")
print("="*60)

# Salvando o modelo vencedor e o scaler dinamicamente
dump(melhor_modelo_objeto, open('melhor_modelo_producao.pkl', 'wb'))
dump(scaler, open('scaler_diabetes.pkl', 'wb'))
print(f"Arquivo 'melhor_modelo_producao.pkl' gerado com sucesso usando {melhor_nome}!")
