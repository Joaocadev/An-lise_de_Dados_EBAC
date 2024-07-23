# Módulo | Análise de Dados: Data Wrangling II
# Caderno de Exercícios

# Tópicos
# 1.Agregação e Ordenação;
# 2.Combinação;
# 3.Técnicas Avançadas.

# Neste exercícios, vamos trabalhar com dados geográficos, demográficos e econômicos do Brasil. Vamos manipular e combinar dados de duas frentes distintas para poder responder perguntas de negócios.

# 1. Data Wrangling
# 1.1. Estados
# O arquivo estados-bruto.xml contém informações sobre estados (nome, sigla e região).
# Utilize o pacote Python beautifulsoup4 para extrair os dados do arquivo estados-bruto.xml providenciado. Salve os dados extraidos no arquivo estados-limpo.csv separado por ;.
# ler o arquivo estados-bruto.xml, utilize o xml parser chamado lxml

from bs4 import BeautifulSoup

with open('estados-bruto.xml', mode='r', encoding='utf8') as arquivo:
  fonte = BeautifulSoup(arquivo, 'lxml-xml')

# visualize os resultados

print(fonte.prettify())

# manipule os dados

import pandas as pd

dados = []

for estado in fonte.find_all('ESTADO'):
  nome = estado.find('NOME').text.strip()
  sigla = estado.find('SIGLA').text.strip()
  regiao = estado.find('REGIAO').text.strip()
  dados.append({'estado': nome, 'sigla': sigla, 'regiao': regiao})

for dado in dados:
    print(dado)

# escrever o conteudo extraido no arquivo estados-limpo.csv separados por ;

import pandas as pd

novo_arquivo = pd.DataFrame(dados, columns=['estado', 'sigla', 'regiao'])
novo_arquivo.to_csv('estados-limpo.csv', sep=';', index=False)

# 1.2. Cidades
# O arquivo cidades-bruto.csv contém informações demográficas e socioeconomicas das cidades do Brasil. Carregue-o na máquina virtual do Google Colab. Utilize o pacote Python pandas para extrair os dados do arquivo cidades-bruto.xml providenciado. Seguindo as seguintes especificações:
# 1.Apenas dados do censo de 2010;
# 2.Apenas as colunas UF, Nome, PIB, Pop_est_2009 e PIB_percapita.
# Salve os dados extraidos no arquivo cidades-limpo.csv separado por ;.
# ler o arquivo cidades-bruto.csv

import pandas as pd

fonte_df = pd.read_csv("cidades-bruto.csv")

# visualize os resultados

print(fonte_df.head())

!pip install unidecode

# manipule os dados

from unidecode import unidecode

fonte_df.rename(columns={'UF': 'estado',
                         'nome': 'cidade',
                         'PIB': 'pib', 'Pop_est_2009':
                         'populacao', 'PIB_percapita':
                         'pib_percapita'}, inplace=True)

censo_df = fonte_df[fonte_df['Censo'] == 2010]

colunas_desejadas = ['estado', 'cidade', 'populacao', 'pib', 'pib_percapita']
cidades_limpo = censo_df[colunas_desejadas]

cidades_limpo['estado'] = cidades_limpo['estado'].apply(unidecode)

# escrever o conteudo extraido no arquivo cidades-limpo.csv separados por ;

cidades_limpo.to_csv('cidades-limpo.csv', sep=';', index=False)

# 1.3. Brasil
# Utilize o pacote Python pandas para combinar os dados do arquivo estados-limpo.csv com os dados do arquivo cidades-limpo.csv em um único dataframe. Escolha a coluna e o método de combinação de tal forma que não haja perda de dados no processo (não produzirá valores nulos NaN). Salve os dados do dataframe no arquivo brasil.csv
# solução do exercício 1.3

import pandas as pd

df_estados = pd.read_csv('estados-limpo.csv', sep=';')
df_cidades = pd.read_csv('cidades-limpo.csv', sep=';')

novo_dataframe = pd.merge(left=df_cidades, right=df_estados, on='estado', how='inner')

novo_dataframe.to_csv('brasil.csv', sep=';', index=False)

print(df_estados.columns)
print(df_cidades.columns)

# 2. Data Analytics
# 2.1. DataFrame
# Utilize o pacote Python pandas para carregar o arquivo brasil.csv no dataframe brasil_df.
# solução do exercício 2.1

import pandas as pd

brasil_df = pd.read_csv('brasil.csv', sep=';')

# 2.2. Analise
# Utilize o dataframe brasil_df para responder as seguintes perguntas de negócio:
# Quais são as 10 cidades mais populosas do Brasil?
# código para responder a pergunta

populacao_df = brasil_df.sort_values(by='populacao', ascending=False)
populacao_df = populacao_df.head(10)

populacao_df

# Quais são as 5 cidades com a menor PIB per capita da região nordeste?
# código para responder a pergunta

pib_df = brasil_df.sort_values(by='pib_percapita', ascending=True)
pib_df = pib_df.head(5)

pib_df

# Quais são as 15 cidades com maior PIB do do estado de São Paulo?
# código para responder a pergunta

df_sp = brasil_df[brasil_df['estado'] == 'SAO PAULO']

pib_sp_df = df_sp.sort_values(by='pib', ascending=False)
pib_sp_df = pib_sp_df.head(15)

pib_sp_df

# Qual é o PIB do estado de Santa Catarina?
# código para responder a pergunta

df_sc = brasil_df[brasil_df['estado'] == 'SANTA CATARINA']

pib_sc_total = df_sc['pib'].sum()
pib_sc_total

# Qual é o população da região sul?
# código para responder a pergunta

df_sul = brasil_df[brasil_df['estado'].isin(['PARANA', 'RIO GRANDE DO SUL', 'SANTA CATARINA'])]

pop_sul_total = df_sul['populacao'].sum()
pop_sul_total

# Qual é o PIB per capito médio das cidades do Mato Grosso do Sul?
# código para responder a pergunta

df_ms = brasil_df[brasil_df['estado'] == 'MATO GROSSO DO SUL']

pib_percapita_med_ms = df_ms['pib_percapita'].mean()
pib_percapita_med_ms

# Qual é a população do Brasil?
# código para responder a pergunta

df_brasil_pop = brasil_df['populacao'].sum()
df_brasil_pop

# 2.3. Visualização
# Utilize o dataframe brasil_df para gerar as seguintes visualizações.
# Gere um gráfico de barras com as 10 cidades menos populosas do Brasil.
# código para gerar a visualização

import matplotlib.pyplot as plt

top_10_menos_pop = brasil_df.nsmallest(10, 'populacao')

plt.figure(figsize=(10, 8))
plt.barh(top_10_menos_pop['cidade'], top_10_menos_pop['populacao'], color='skyblue')
plt.xlabel('Populacao')
plt.ylabel('Cidade')
plt.title('10 Cidades menos populosas do Brasil')
plt.gca().invert_yaxis()
plt.show()

# Gere um gráfico de pizza com a proporção da população do Brasil por região.
# código para gerar a visualização

import matplotlib.pyplot as plt

pop_por_regiao = brasil_df.groupby('regiao')['populacao'].sum()
plt.figure(figsize=(10, 7))
plt.pie(pop_por_regiao, labels=pop_por_regiao.index, autopct='%1.1f%%', startangle=140)
plt.title('Proporção da população do Brasil por região')
plt.axis('equal')
plt.show()