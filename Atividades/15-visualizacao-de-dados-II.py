# Módulo | Análise de Dados: Visualização de Dados II
# Caderno de Exercícios

# Tópicos
# 1.Distribuições: Histograma, KDE e Box Plot;
# 2.Correlação: Gráfico de Disperção e Mapa de Calor.
# Nestes exercícios, você deve decidir qual é o gráfico visto em aula que melhor visualiza uma base de dados. Após decidir, você deverá criar a visualização usando o conteúdo exposto durante a aula e adicionar um pequeno parágrafo sobre um insights que pode ser extraido do gráfico.

# 1. Preços outliers de diamante

import seaborn as sns

data = sns.load_dataset("diamonds")
data.head()

# gráfico do exercício 1

with sns.axes_style('whitegrid'):

  grafico = sns.boxplot(x=data['price'])
  grafico.set(title='Preço do diamante', xlabel='Preço (USD)')

# Insight do gráfico 1: Através do gráfico gerado, é possivel afirmar que a média do valor do diamante está em torno 2400 a 2500, as hastes que se estendem acima dos 5 mil dolares indica que não é tão comum consumidores pagarem mais que 5 mil dolares pelo diamante, acima dos 12 mil dolares é menos comum ainda.

# 2. Correlação entre o do preço do diamante com seu peso (carat) agrupados por sua transparêcia (clarity)

import seaborn as sns

data = sns.load_dataset("diamonds")
data.head()

# gráfico do exercício 2

diamonds = data[['carat', 'clarity', 'price']]
diamonds = diamonds.query('price < 500')
diamonds.head()

with sns.axes_style('whitegrid'):

  grafico = sns.scatterplot(data=diamonds, x='price', y='carat', hue='clarity')
  grafico.set(title='Preço do diamante', xlabel='Preço (USD)', ylabel='Peso');
  grafico.get_legend().set_title('Claridade')

# Insight do gráfico 2: Percebo pelo gráfico que não tem um padrão muito claro no aumento do preço, se é devido à claridade do diamante ou ao peso, mas percebo que quanto maior o peso, maior o preço.

# 3. Distribuição contínua aproximada do peso (weight) de carros

import seaborn as sns

data = sns.load_dataset("mpg")
data.head()

# gráfico do exercício 3

with sns.axes_style('whitegrid'):

  grafico = sns.histplot(data=data, x='weight', kde=True)
  grafico.set(title='Distribuição contínua aproximada do peso de carros', xlabel='Peso (libras)')

# Insight do gráfico 3: Percebe-se que a tendência tende a diminuiar na contagem dos carros por peso, tem um volume maior de carros com aproximadamente 2000 libras e a contagem diminui de acordo com que o peso aumenta.