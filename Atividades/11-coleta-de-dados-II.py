# Módulo | Análise de Dados: Coleta de Dados II
# Caderno de Exercícios

# Tópicos
# 1.Web Crawling;
# 2.Web Scraping.

# 1. Filmes populares do IMDB
# O IMDB é um famoso site de reviews de filmes e seriados. Uma das páginas mais acessadas do website é o ranking de filmes mais bem votados. Neste exercício, vamos extrair informações deste website.

# 1.1. Arquivo Robots.txt
# Utilize o pacote Python requests para fazer o download do conteúdo do arquivo robots.txt do site do IMDB e salve numa variável chamada robots.
# Com o conteúdo na variável robots, verifique se a palavra top ou charts está presente no conteúdo do texto. Se sim, imprima True, senão imprima False.

import requests

robots = requests.get('https://www.imdb.com/robots.txt')
print(robots.status_code)

if 'top' and 'charts' in robots:
  print(True)
else:
  print(False)

# 1.2. Crawling & Scraping
# Utilize os pacotes Python requests e beautifulsoup4 para extrair os 10 filmes mais populares do IMDB (titulo, ano e nota).
# Escreva os dados extraídos no arquivo csv imdb.csv separado por ;.

# a) Utilize o pacote requests para fazer o download da página na variável conteudo

import requests
from requests.exceptions import HTTPError

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Accept-Language': 'en-US,en;q=0.5'
    }

conteudo = None
URL = 'https://www.imdb.com/chart/top'

try:
    resposta = requests.get(URL, headers=headers)
    resposta.raise_for_status()
except HTTPError as exc:
    print(exc)
else:
    conteudo = resposta.text

    print(conteudo)

# b) Utilize o pacote beautifulsoup4 para carregar o HTML da variavel conteudo na variavel pagina

from bs4 import BeautifulSoup

pagina = BeautifulSoup(conteudo, 'html.parser')

# c) Utilize o código abaixo para iterar nas linhas e colunas da tabela e preencher a variavel conteudo_extraido

conteudo_extraido = []

lista_filmes = pagina.find_all('li',{'class':'ipc-metadata-list-summary-item'})

for filme in lista_filmes:
  textos_coluna = []

  titulo_ranking = filme.find('h3', {'class': 'ipc-title__text'})
  if titulo_ranking:
    titulo_ranking = titulo_ranking.get_text().strip().replace('\xa0', ' ')
    ranking, titulo = titulo_ranking.split('. ', 1)
    textos_coluna.append(ranking)
    textos_coluna.append(titulo)

  ano = filme.find('span', {'class': 'sc-b189961a-8 kLaxqf cli-title-metadata-item'}).get_text().strip().replace('\xa0', ' ')
  textos_coluna.append(ano)

  avaliacao_imdb = filme.find('span', {'class': 'ipc-rating-star--imdb'}).get_text().strip().replace('/xa0', ' ')
  textos_coluna.append(avaliacao_imdb.split(' ')[0])

  conteudo_extraido.append(textos_coluna)

  conteudo_extraido = conteudo_extraido[:10]

# d) Escreva o arquivo imdb.csv com o conteudo da variavel conteudo_extraido

import pandas as pd

top_10_filmes= pd.DataFrame(conteudo_extraido, columns=['Ranking', 'Titulo', 'Ano', 'Avaliacao'])
top_10_filmes.to_csv('imdb_top_10.csv', index=False)