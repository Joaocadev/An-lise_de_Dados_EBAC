# Módulo | Módulos e pacotes
# Caderno de Exercícios

# Tópicos
# 1.from / import / as;
# 2.Módulo;
# 3.Pacote;
# 4.Baixando pacotes.

# 1.Vamos importar o pacote com o apelido (alias) pd.

import pandas as pd

df = pd.read_csv('./dados/dow_jones_index.csv')

# Visualizando as n primeiras linhas:
df.head(n=10)

# Visualizando o nome das colunas:
df.columns.to_list()

# Verificando o número de linhas e colunas.
linhas, colunas = df.shape
print(f'Número de linhas: {linhas}')
print(f'Número de colunas: {colunas}')

# Vamos selecionar os valores de abertura, fechamento, máximo e mínimo das ações do McDonalds, listado na Dow Jones como MCD:
# Selecionando as linha do dataframe original df em que a coluna stock é igual a MCD.

df_mcd = df[df['stock'] == 'MCD']

# Selecionando apenas as colunas de data e valores de ações.

df_mcd = df_mcd[['date', 'open', 'high', 'low', 'close']]

# Vamos limpar as colunas com o método apply, que permite a aplicação de uma função anônima (lambda) qualquer. A função lambda remove o caracter $ e faz a conversão do tipo de str para float.

for col in ['open', 'high', 'low', 'close']:
  df_mcd[col] = df_mcd[col].apply(lambda value: float(value.split(sep='$')[-1]))

# Selecionando as linha do dataframe original df em que a coluna stock é igual a KO.

df_ko = df[df['stock'] == 'KO']

# Vamos selecionar os valores de abertura, fechamento, máximo e mínimo das ações da empresa Coca-Cola, listado na Dow Jones como KO:
# Selecionando apenas as colunas de data e valores de ações.

df_ko = df_ko[['date', 'open', 'high', 'low', 'close']]

# Vamos limpar as colunas com o método apply, que permite a aplicação de uma função anônima (lambda) qualquer. A função lambda remove o caracter $ e faz a conversão do tipo de str para float.

for coluna in ['open', 'high', 'low', 'close']:
  df_ko[coluna] = df_ko[coluna].apply(lambda value: float(value.split(sep='$')[-1]))

# 2. Seaborn
# Vamos importar o pacote com o apelido (alias) sns.

import seaborn as sns

# Vamos visualizar os valores de abertura das ações ao longo do tempo.

plot = sns.lineplot(x="date", y="open", data=df_mcd)
_ = plot.set_xticklabels(labels=df_mcd['date'], rotation=90)

# Vamos também visualizar os valores de fechamento das ações ao longo do tempo.

plot = sns.lineplot(x="date", y="close", data=df_mcd)
_ = plot.set_xticklabels(labels=df_mcd['date'], rotation=90)

# Para facilitar a comparação, vamo visualizar os quatro valores no mesmo gráfico.

plot = sns.lineplot(x="date", y="value", hue='variable', data=pd.melt(df_mcd, ['date']))
_ = plot.set_xticklabels(labels=df_mcd['date'], rotation=90)

# Para finalizar, vamos salvar o gráfico numa figura.

plot.figure.savefig("./mcd.png")

# Visualização dos dados da Coca-Cola.

plot = sns.lineplot(x='date', y='value', hue='variable', data=pd.melt(df_ko, ['date']))
_ = plot.set_xticklabels(labels=df_ko['date'], rotation=90)

# Vamos visualizar os valores de abertura das ações ao longo do tempo.

plot = sns.lineplot(x="date", y="open", data=df_ko)
_ = plot.set_xticklabels(labels=df_ko['date'], rotation=90)

# Vamos também visualizar os valores de fechamento das ações ao longo do tempo.

plot = sns.lineplot(x="date", y="close", data=df_ko)
_ = plot.set_xticklabels(labels=df_ko['date'], rotation=90)

# Para facilitar a comparação, vamo visualizar os quatro valores no mesmo gráfico.

plot = sns.lineplot(x='date', y='value', hue='variable', data=pd.melt(df_ko, ['date']))
_ = plot.set_xticklabels(labels=df_ko['date'], rotation=90)

# Para finalizar, vamos salvar o gráfico numa figura.

plot.figure.savefig("./ko.png")