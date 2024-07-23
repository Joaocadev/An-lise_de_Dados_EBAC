# Módulo | Análise de Dados: Visualização de Dados I
# Caderno de Exercícios

# Tópicos
# 1.Pacote Seaborn;
# 2.Categorias: Gráficos de Barras e de Setores;
# 3.Tendências: Gráficos de Linha e de Área.

# Nestes exercícios, você deve decidir qual é o gráfico visto em aula que melhor visualiza uma base de dados. Após decidir, você deverá criar a visualização usando o conteúdo exposto durante a aula e adicionar um pequeno parágrafo sobre um insights que pode ser extraido do gráfico.
# 1. Preço do diamante por tipo de corte

import seaborn as sns

data = sns.load_dataset("diamonds")
data.head()

# gráfico do exercício 1

diamonds = data[['cut', 'price']].groupby('cut').agg('sum').reset_index()
diamonds.head()

grafico = sns.barplot(data=data, x='cut', y='price', ci=None)
grafico.set(title='Preço do diamante por tipo de corte', xlabel='Corte', ylabel='Preço')

# Insight do gráfico 1: Percebe-se que o corte "premium" é o mais caro, enquanto o corte "ideal" é o mais barato, possivelmente devido a qualidade final que é inferior aos demais tipos de corte.

# 2. Número de passageiros em dezembro por ano

import seaborn as sns

data = sns.load_dataset("flights")
data.head()

# gráfico do exercício 2

flights = data[['year', 'month', 'passengers']].groupby(['year', 'month']).agg('sum').reset_index()
flights.head()

mes = data.query('month == "Dec"')
mes.head()

with sns.axes_style('whitegrid'):

    grafico = sns.lineplot(data=mes, x='year', y='passengers', hue='month', ci=None)
    grafico.set(title='Número de passageiros em dezembro por ano', xlabel='Ano', ylabel='Passageiros')

# Insight do gráfico 2: É possivel perceber que ao decorrer dos anos o gráfico tem uma grande crescente de passageiros no mês de dezembro, entre os anos de 1957 e 1958 é possível observar que da uma estabilizada mas logo volta a crescer.

# 3. Numero de passageiros por mês entre 1949 e 1959

import seaborn as sns

data = sns.load_dataset("flights")
data.head()

# gráfico do exercício 3

flights = data[['year', 'passengers']].groupby('year').agg('sum').reset_index()
flights.head()

voos = data.query('1949 <= year < 1959')

with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=voos, x='month', y='passengers', hue='year', ci=None)
  grafico.set(title='Número de passageiros por mês entre 1949 e 1959', xlabel='Meses', ylabel='Passageiros')
  grafico.get_legend().set_title('Ano')

# Insight do gráfico 3: É possivel perceber que o gráfico tem uma constante crescente, porém nos meses de fevereiro e novembro vemos uma grande baixa no número de passageiros durante os anos.