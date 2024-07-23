# Módulo | Análise de Dados: Data Wrangling I
# Caderno de Exercícios

# Tópicos
# 1.DataFrame Pandas;
# 2.Selecão e Filtros;
# 3.Inserção, Deleção e Atualização.

# 1. Fortune 500
# O Fortune 500 é uma ranking anual compilado pela revista Fortune das 500 maiores empresas dos EUA.
# O arquivo fortune.html contem o código fonte em HTML da página com as 100 primeiras empresas do ranking.
# Utilize o pacote Python beautifulsoup4 para extrair todas as 100 empresas do arquivo fortune.html providenciado. Salve os dados extraidos no arquivo fortune.csv separado por ;.

# ler o arquivo fortune.html

from bs4 import BeautifulSoup

with open('fortune.html', mode='r', encoding='utf8') as arquivo:
  pagina = BeautifulSoup(arquivo, 'html.parser')

# extrair as linhas da tabela

tabela = pagina.find('div', {'class': 'rt-table'})
linhas = tabela.find('div', {'class': 'rt-tbody'})

# extrair o conteudo das linhas da tabela

conteudo_extraido = []

for linha in linhas:
  colunas = linha.find('div', {'role': 'row'})
  conteudo = colunas.get_text(';').split(';')
  conteudo_extraido.append(conteudo)
  print(conteudo)

# escrever o conteudo extraido no arquivo fortune.csv
# utilize a variavel header para construir a o cabecalho do arquivo csv

header = [
  'rank',
  'name',
  'revenues',
  'revenues-percent-change',
  'profits',
  'profits-percent-change',
  'assets',
  'market-value',
  'employees'
]

import pandas as pd

top_100 = pd.DataFrame(conteudo_extraido, columns=header)
top_100.to_csv('fortune.csv', index=False)

# 2. Data Wrangling
# 2.1. Criando o DataFrame
# Crie o dataframe Pandas na variável fortune_df através da leitura do arquivo fortune.csv

import pandas as pd

fortune_df = pd.read_csv('fortune.csv')

# 2.2. Explorando o DataFrame
# Utilizando os métodos vistos em aula, explore o dataframe.
# Liste as 10 primeiras linhas do dataframe:

top_10_linhas = fortune_df.loc[0:9]
top_10_linhas

# Liste os tipos de dados armazenados na coluna do dataframe:

fortune_df.dtypes

# Liste o numero de linhas e colunas do dataframe:

fortune_df.shape

# 2.3. Limpando o DataFrame
# Grande parte das colunas numéricas (exceto a coluna ranking e employees) possuem o caracter $ ou % que as classificam com o tipo object (ou str do Python) ao invés do tipo correto como int ou float. Utilizando os métodos de atualizam, remova os caracteres das linhas das colunas numéricas.

numericos = ['revenues', 'revenues-percent-change', 'profits', 'profits-percent-change', 'assets', 'market-value']

fortune_df[numericos] = fortune_df[numericos].replace('[$%]', "", regex=True)

# 2.4. Salvando o DataFrame
# Utilize o método to_csv para salvar o dataframe fortune_df no arquivo fortune-limpo.csv.

fortune_limpo = pd.DataFrame(fortune_df)
fortune_limpo.to_csv('fortune_limpo.csv', index=False)