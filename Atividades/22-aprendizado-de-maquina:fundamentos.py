# Módulo | Análise de Dados: Fundamentos de Aprendizado de Máquina
# Caderno de Exercícios

# Tópicos
# 1.Teoria;
# 2.Atributos categóricos;
# 3.Atributos numéricos;
# 4.Dados faltantes.

# 1. Pinguins
# Neste exercício, vamos utilizar uma base de dados com informações sobre penguins. A idéia é preparar a base de dados para prever a espécie do penguin (variável resposta) baseado em suas características físicas e geográficas (variáveis preditivas).

import numpy as np
import pandas as pd
import seaborn as sns

data = sns.load_dataset('penguins')

data.head()

data.shape

# 1.1. Valores nulos
# A base de dados possui valores faltantes, utilize os conceitos da aula para trata-los.

# Aplica o método "dropna" para remover as linhas que possuem valores nulos.

data.dropna(inplace=True)
data.head()

# Uso comando para comparar a quantidade de linhas e colunas com o dataframe original.

data.shape

# Certifico de que não possua mais valores nulos.

data.isnull().sum()

# 1.2. Variáveis numéricas
# Identifique as variáveis numéricas e crie uma nova coluna padronizando seus valores. A nova coluna deve ter o mesmo nome da coluna original acrescidade de "_std".

# Aplica a função lambda para realizar a padronização, dividindo o valor da média pelo desvio padrão.

data["bill_length_mm_std"] = data["bill_length_mm"].apply(lambda valor: (valor - data["bill_length_mm"].mean()) / data["bill_length_mm"].std())
data["bill_depth_mm_std"] = data["bill_depth_mm"].apply(lambda valor: (valor - data["bill_depth_mm"].mean()) / data["bill_depth_mm"].std())
data["flipper_length_mm_std"] = data["flipper_length_mm"].apply(lambda valor: (valor - data["flipper_length_mm"].mean()) / data["flipper_length_mm"].std())
data["body_mass_g_std"] = data["body_mass_g"].apply(lambda valor: (valor - data["body_mass_g"].mean()) / data["body_mass_g"].std())

data.head()

# 1.3. Variáveis categóricas
# Identifique as variáveis categóricas nominais e ordinais, crie uma nova coluna aplicando a técnica correta de conversão a seus valores. A nova coluna deve ter o mesmo nome da coluna original acrescidade de "_nom" ou "_ord".

# Aplica a função lambda para padronizar os valores categóricos de forma binária, ou seja, 0 e 1.

data["island_nom_Torgersen"] = data["island"].apply(lambda valor: 1 if valor == "Torgersen" else 0)
data["island_nom_Biscoe"] = data["island"].apply(lambda valor: 1 if valor == "Biscoe" else 0)
data["island_nom_Dream"] = data["island"].apply(lambda valor: 1 if valor == "Dream" else 0)

data["sex_nom_M"] = data["sex"].apply(lambda valor: 1 if valor == "Male" else 0)
data["sex_nom_F"] = data["sex"].apply(lambda valor: 1 if valor == "Female" else 0)

data.head()

# 1.4. Limpeza
# Descarte as colunas originais e mantenha apenas a variável resposta e as variáveis preditivas com o sufixo _std", _nom" e "_ord".

# Aplica a função drop para remover as colunas originais do dataframe e mantém apenas as colunas padronizadas.

data.drop(["island", "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "sex"], axis=1, inplace=True)
data.head()