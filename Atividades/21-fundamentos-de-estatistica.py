# Módulo | Análise de Dados: Fundamentos de Estatística
# Caderno de Exercícios

# Tópicos
# 1.Média e Variância;
# 2.Ordem e Posição;
# 3.Correlação.

# 1. Tráfego de São Paulo
# Neste exercício, vamos continuar a analisar os dados de mobilidade urbana da cidade de São Paulo. A base de dados contem a quantidade de acidentes ocorridos na cidade entre 14/12/09 e 18/12/09, das 07:00h ás 20:00h, agregados em intervalos de 30 minutos.

import pandas as pd

df = pd.read_csv('traffic.csv', sep=';')

df.head()

# O código abaixo extrai a 13ª linha do arquivo que representa a 14ª meia hora do dia 14/12/09, contadas a partir das 07:00h, ou seja, todos os incidentes ocorridos na cidade no dia em questão entre as 13:30h e 14:00h. Vemos, por exemplo, que dois ônibus e dois caminhões ficaram paradados nas ruas da cidade, atrapalhando o tráfego.

df.iloc[[13]]

# 1.1. Agregação
# Neste primeira atividade, você deve gerar um array NumPy por dia. Para cada array você deve somar todos os incidentes que aconteceram naquela meia hora. Sendo assim, cada array deve ter 27 posições, cada qual com a soma dos incidentes daquela meira hora.
# Dica: Você deve remover a primeira e a última coluna.
# Remove a primeira e a última coluna do dataframe usando comando drop().

import numpy as np

df.drop(columns=['hour', 'slowness_traffic_%'], axis=1, inplace=True)

# Seleciona as linhas de interesse do dataframe e converte em um array de 16 linhas e 27 colunas.

dia_14 = np.array(df.iloc[0:27].T.values.reshape(16,27))
dia_15 = np.array(df.iloc[27:54].T.values.reshape(16,27))
dia_16 = np.array(df.iloc[54:81].T.values.reshape(16,27))
dia_17 = np.array(df.iloc[81:108].T.values.reshape(16,27))
dia_18 = np.array(df.iloc[108:137].T.values.reshape(16,27))

# Soma os arrays criados linha por linha.

dia_14 = np.sum(dia_14, axis=0)
dia_15 = np.sum(dia_15, axis=0)
dia_16 = np.sum(dia_16, axis=0)
dia_17 = np.sum(dia_17, axis=0)
dia_18 = np.sum(dia_18, axis=0)

# 1.2. Métricas
# Para cada array você deve calcular as seguintes métricas:
# média;
# desvio padrão.

# Calcula a média dos valores e arredonda o resultado para 2 casas decimais.

media_dia_14 = round(np.mean(dia_14), 2)
media_dia_15 = round(np.mean(dia_15), 2)
media_dia_16 = round(np.mean(dia_16), 2)
media_dia_17 = round(np.mean(dia_17), 2)
media_dia_18 = round(np.mean(dia_18), 2)

print(f'Média dia 14: {media_dia_14}')
print(f'Média dia 15: {media_dia_15}')
print(f'Média dia 16: {media_dia_16}')
print(f'Média dia 17: {media_dia_17}')
print(f'Média dia 18: {media_dia_18}')

# Calcula o desvio padrão dos valores e arredonda o resultado para 2 casas decimais.

std_dia_14 = round(np.std(dia_14), 2)
std_dia_15 = round(np.std(dia_15), 2)
std_dia_16 = round(np.std(dia_16), 2)
std_dia_17 = round(np.std(dia_17), 2)
std_dia_18 = round(np.std(dia_18), 2)

print(f'Desvio padrão dia 14: {std_dia_14}')
print(f'Desvio padrão dia 15: {std_dia_15}')
print(f'Desvio padrão dia 16: {std_dia_16}')
print(f'Desvio padrão dia 17: {std_dia_17}')
print(f'Desvio padrão dia 18: {std_dia_18}')

# 1.3. Interpretação
# Baseado nos resultados da questão 1.2, responda:
# Qual dia apresenta a maior média de acidentes por meia hora?
# Resposta: O dia que apresenta a maior média de acidentes por meia hora é o dia 16, com uma média de 0.22.

# Qual dia apresenta a menor variação de acidentes por meia hora?
# Resposta: O dia que apresenta a menor variação de acidentes por meia hora é o dia 14, com um desvio padrão de 0.23.