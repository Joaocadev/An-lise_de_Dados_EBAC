# Módulo | Análise de Dados: Análise Exploratória de Dados de Logística II
# Caderno de Exercícios

# Tópicos
# 1.Manipulação;
# 2.Visualização;
# 3.Storytelling.

# Este notebook deve servir como um guia para você continuar a construção da sua própria análise exploratória de dados. Fique a vontate para copiar os códigos da aula mas busque explorar os dados ao máximo.

# Análise Exploratória de Dados de Logística
# 1. Contexto
# A Loggi, uma startup inovadora no setor de logística, enfrenta desafios crescentes devido à variação na densidade demográfica das regiões que atende. Este projeto foca no Distrito Federal, onde a Loggi opera com três centros de distribuição em áreas de diferentes densidades populacionais. Através de um processo completo de data wrangling e a geração de visualizações gráficas, buscamos extrair insights operacionais cruciais para otimizar as operações logísticas da empresa.

# 2. Pacotes e bibliotecas
# Pacotes e bibliotecas usados no projeto.

!pip install geopandas

import json

import pandas as pd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import numpy as np
import geopandas
import matplotlib.pyplot as plt
import seaborn as sns

# 3. Exploração de dados
# 3.1 Carregando os dados
# Lê o arquivo json e armazena os dados na variável data.

with open("deliveries.json", mode="r", encoding="utf8") as file:
  data = json.load(file)

# Transforma o arquivo json em um data frame e imprime as 5 primeiras linhas.

deliveries_df = pd.DataFrame(data)
deliveries_df.head()

# 3.2 Data Wrangling
# Percebe-se que na coluna origin do DataFrame há dados aninhados, é necessário usar o método json_normalize do pandas para normalizar a coluna com uma operação chamada flatten ou achatamento para separar essas informações em colunas de um novo DataFrame.
# Separa a coluna "origin" em duas colunas, lng e lat.

origin_hub_df = pd.json_normalize(deliveries_df["origin"])
origin_hub_df.head()

# Com um novo DataFrame gerado, podemos mesclar ao DataFrame original e remover a coluna origin.
# Une as colunas separadas anteriormente no DataFrame original.

deliveries_df = pd.merge(left=deliveries_df, right=origin_hub_df, how="inner", left_index=True, right_index=True)

# Remove a coluna "origin", reorganiza as colunas e renomea as novas colunas do DataFrame.

deliveries_df = deliveries_df.drop("origin", axis=1)
deliveries_df = deliveries_df[["name", "region", "lng", "lat", "vehicle_capacity", "deliveries"]]
deliveries_df = deliveries_df.rename(columns={"lng": "hub_lng", "lat": "hub_lat"})
deliveries_df.head()

# Ainda há dados aninhados na coluna deliveries, nesse caso usaremos o método explode do pandas para transformar elementos de uma lista que estão armazenados em uma única célula de um DataFrame em linhas individuais mantendo o índice original, após isso separamos as informações em novas colunas e DataFrames novos.
# Normaliza a coluna "deliveries" com explode, transformando cada elemento em uma nova coluna.

deliveries_explode_df = deliveries_df[["deliveries"]].explode("deliveries")
deliveries_explode_df.head()

# Cria um novo DataFrame e transforma cada elemente da lista em uma nova coluna.

deliveries_normalized_df = pd.concat([
    pd.DataFrame(deliveries_explode_df["deliveries"].apply(lambda record: record["size"])).rename(columns={"deliveries": "deliveries_size"}),
    pd.DataFrame(deliveries_explode_df["deliveries"].apply(lambda record: record["point"]["lng"])).rename(columns={"deliveries": "deliveries_lng"}),
    pd.DataFrame(deliveries_explode_df["deliveries"].apply(lambda record: record["point"]["lat"])).rename(columns={"deliveries": "deliveries_lat"}),
], axis=1)

# Verifica o tamanho do novo DataFrame gerado.

len(deliveries_explode_df)

# Verifica o tamanho do DataFrame original.

len(deliveries_df)

# Mescla o novo DataFrame explodido com o DataFrame original, junção feita através do índice right.

deliveries_df = deliveries_df.drop("deliveries", axis=1)
deliveries_df = pd.merge(left=deliveries_df, right=deliveries_normalized_df, how="right", left_index=True, right_index=True)
deliveries_df.reset_index(inplace=True, drop=True)
deliveries_df.head()

# Verifica o tamanho novamente do DataFrame original.

len(deliveries_df)

# 4. Manipulação
# 4.1 Enriquecimento
# Geocodificação reversa do Hub
# A geocodificação é o processo que transforma uma localização descrita por um texto (endereço, nome do local, etc.) em sua respectiva coodernada geográfica (latitude e longitude). A geocodificação reversa faz o oposto, transforma uma coordenada geográfica de um local em suas respectivas descrições textuais.

# Seleciona colunas de interesse do DataFrame original e remove valores duplicados.

hub_df = deliveries_df[["region", "hub_lng", "hub_lat"]]
hub_df = hub_df.drop_duplicates().sort_values(by="region").reset_index(drop=True)

# Usa a geocodificação reversa para transformar as coordenadas geográfica dos hub's em um local com suas respectivas descrições textuais.

geolocator = Nominatim(user_agent="ebac_geocoder")
location = geolocator.reverse("-15.657014, -47.802665")

print(json.dumps(location.raw, indent=2, ensure_ascii=False))

# Vamos então aplicar a geocodificação nas coordenadas das três regiões e extrair informações de cidade e bairro. Criamos uma nova coluna "coordinates" para a combinação das colunas hub_lng e hub_lat separadas por vírgula. A coluna geodata retorna as informações textuais da geocodificação reversa.
# Aplica a geocodificação nas 3 coordenadas dos centros de distribuição e cria uma nova coluna "coordinates" com as coordenadas do "hub_lng e "hub_lat.

geocoder = RateLimiter(geolocator.reverse, min_delay_seconds=1)

hub_df["coordinates"] = hub_df["hub_lat"].astype(str)  + ', ' + hub_df["hub_lng"].astype(str)
hub_df["geodata"] = hub_df["coordinates"].apply(geocoder)
hub_df.head()

# Aplicamos novamente o método json_normalize do pandas para normalizar a coluna geodata para separar essas informações em colunas de um novo DataFrame.
# Aplica o método json_normalize na coluna "geodata".

hub_geodata_df = pd.json_normalize(hub_df["geodata"].apply(lambda data: data.raw))
hub_geodata_df.head()

# No DataFrame que geramos, identificamos três colunas de interesse: "address.suburb", "address.town" e "address.city". Para tornar nossos dados mais claros e organizados, vamos renomear essas colunas para "hub_suburb", "hub_town" e "hub_city".
# Agora, aqui está o plano para garantir que nossos dados estejam completos: primeiro, verificaremos a coluna "hub_city". Se encontrarmos algum valor vazio, preencheremos essa lacuna com o dado correspondente da coluna "hub_town". Em seguida, faremos o mesmo para "hub_suburb". Se houver alguma entrada ausente em "hub_suburb", preencheremos com o valor de "hub_city".
# Essa abordagem garantirá que nosso DataFrame esteja sempre completo e preparado para análises mais profundas, mantendo nossos dados precisos e consistentes.
# Renomea as colunas e substitui valores vazios por valores do hub_town e hub_city.

hub_geodata_df = hub_geodata_df[["address.town", "address.suburb", "address.city"]]
hub_geodata_df.rename(columns={"address.town": "hub_town", "address.suburb": "hub_suburb", "address.city": "hub_city"}, inplace=True)
hub_geodata_df["hub_city"] = np.where(hub_geodata_df["hub_city"].notna(), hub_geodata_df["hub_city"], hub_geodata_df["hub_town"])
hub_geodata_df["hub_suburb"] = np.where(hub_geodata_df["hub_suburb"].notna(), hub_geodata_df["hub_suburb"], hub_geodata_df["hub_city"])
hub_geodata_df = hub_geodata_df.drop("hub_town", axis=1)
hub_geodata_df.head()

# Vamos mesclar os DataFrames hub_df e hub_geodata_df usando o método merge do pandas com a junção pelos índices. Em seguida, integraremos o resultado ao DataFrame original utilizando o método de junção "inner", garantindo que todas as entradas correspondentes de ambos os DataFrames sejam combinadas. Por fim, reorganizaremos as colunas para manter tudo bem estruturado.
# Mescla os novos DataFrames a partir dos índices.

hub_df = pd.merge(left=hub_df, right=hub_geodata_df, left_index=True, right_index=True)
hub_df = hub_df[["region", "hub_suburb", "hub_city"]]
hub_df.head()

# Mescla os novos DataFrames ao original e reorganiza as colunas.

deliveries_df = pd.merge(left=hub_df, right=deliveries_df, how="inner", on="region")
deliveries_df = deliveries_df[["name", "region", "hub_lng", "hub_lat", "hub_city", "hub_suburb", "vehicle_capacity", "deliveries_size", "deliveries_lng", "deliveries_lat"]]
deliveries_df.head()

# Enquanto o hub contem apenas 3 geolocalizações distintas, as entregas somam o total de 636.149, o que levaria em torno de 7 dias para serem consultadas no servidor do Nominatim, dada a restrição de uma consulta por segundo. Contudo, para cargas pesadas como esta, o software oferece uma instalação local (na sua própria máquina) que pode ser utilizada sem restrição. Dessa forma, o acesso ao conteúdo já geocodificado foi disponibilizado por meio do arquivo na pasta.
# Carrega um novo DataFrame com as 636.149 mil geocoficações.

deliveries_geodata_df = pd.read_csv("deliveries-geodata.csv")
deliveries_geodata_df.head()

# Mescla o novo DataFrame com as geocodificações com o DataFrame original a partir do índice.

deliveries_df = pd.merge(left=deliveries_df, right=deliveries_geodata_df[["delivery_city", "delivery_suburb"]], how="inner", left_index=True, right_index=True)
deliveries_df.head()

# Ver as dimensões do DataFrame, sendo 636149 o número de linhas e 12 o número de colunas.

deliveries_df.shape

# Verifica se alguma coluna possui dado faltante.

deliveries_df.isna().sum()

# Verifica valores únicos nas colunas.

deliveries_df.nunique()

# Conhecer os tipos de dados e colunas.

deliveries_df.info()

# Ver resumo estatístico dos dados numéricos.

deliveries_df.describe().T

# Observações a serem feitas: 1: Os dados da coluna "vehicle_capaty" não apresentam variações, significa que todos os valores são iguais. 2: Os valroes da coluna "delivery_size" mostram que os volumes variam moderadamente, com uma média de 5.5121 e uma mediana de 6.0000, logo, desvio padrão de 2.8746, considerando a baixa amplitude, são variações relativamente moderadas. 3: A coluna "delivery_city" possui 1702 dados nulos, quanto a coluna "delivery_suburb" possui 159885 dados nulos.

# Ver resumo dos dados categóricos.

deliveries_df.select_dtypes("object").describe().transpose()

# 4: O centro de distribuição que possui mais demandas é o df-1, com 304708 registros.

# Ver a porcentagem de valores nulos na coluna "delivery_city".

100 * (deliveries_df["delivery_city"].isna().sum() / len(deliveries_df))

# Ver a porcentagem de valores nulos na coluna "delivery_suburb".

100 * (deliveries_df["delivery_suburb"].isna().sum() / len(deliveries_df))

# Ver a procentagem de valores nulos na coluna "delivery_city" separados por cidades do Distrito Federal.

prop_df = deliveries_df[["delivery_city"]].value_counts() / len(deliveries_df)
prop_df.sort_values(ascending=False).head(10)

# Ver a porcentagem de valores nulos na coluna "delivery_suburb" separados por bairros do Distrito Federal.

prop_df = deliveries_df[["delivery_suburb"]].value_counts() / len(deliveries_df)
prop_df.sort_values(ascending=False).head(10)

# Observações: 1. Observamos que a coluna "delivery_city" possui apenas 0,26% de dados nulos ou NaN, o que é aceitável considerando a quantidade total de dados. Por outro lado, a coluna "delivery_suburb" apresenta 25,13% de dados nulos ou NaN, o que pode comprometer sua utilidade.
# 5. Visualização
# 5.1 Mapa de Entregas por Região
# Vamos fazer o download dos dados do mapa do Distrito Federal do site oficial do IBGE para criar o DataFrame mapa.
# Gera um novo DataFrame usando o geopandas.

mapa = geopandas.read_file("distrito-federal.shp")
mapa = mapa.loc[[0]]
mapa.head()

# Cria o DataFrame geo_hub_df através do DataFrame deliveries_df.

hub_df = deliveries_df[["region", "hub_lng", "hub_lat"]].drop_duplicates().reset_index(drop=True)
geo_hub_df = geopandas.GeoDataFrame(hub_df, geometry=geopandas.points_from_xy(hub_df["hub_lng"], hub_df["hub_lat"]))
geo_hub_df.head()

# Cria o DataFrame geo_deliveries_df através do DataFrame deliveries_df.

geo_deliveries_df = geopandas.GeoDataFrame(deliveries_df, geometry=geopandas.points_from_xy(deliveries_df["deliveries_lng"], deliveries_df["deliveries_lat"]))
geo_deliveries_df.head()

# 5.2 Visualização do Mapa
# Cria um plot vazio.

fig, ax = plt.subplots(figsize = (50/2.54, 50/2.54))

# Plot com o mapa do Distrito Federal.

mapa.plot(ax=ax, alpha=0.4, color="lightgrey")

# Plot com as entregas.

geo_deliveries_df.query("region == 'df-0'").plot(ax=ax, markersize=1, color="red", label="df-0")
geo_deliveries_df.query("region == 'df-1'").plot(ax=ax, markersize=1, color="blue", label="df-1")
geo_deliveries_df.query("region == 'df-2'").plot(ax=ax, markersize=1, color="seagreen", label="df-2")

# Plot com os hubs

geo_hub_df.plot(ax=ax, markersize=40, marker="x", color="black", label="hub")

# Cria a legenda

plt.title("Entregas no Distrito Deferal por Região", fontdict={"fontsize": 16})
lgnd = plt.legend(prop={"size": 15})
for handle in lgnd.legendHandles:
  handle.set_sizes([50])

# Insights:
# As entregas dos hubs DF-0 e DF-2 estão mais distribuídas, o que pode resultar em um tempo maior de entrega e em gastos elevados.
# Os hubs DF-1 e DF-2 estão melhor localizados, proporcionando maior agilidade no processo de entrega e, consequentemente, economizando recursos.
# O hub DF-0, por atender uma área maior e mais espalhada, pode gerar maiores gastos nas entregas e demandar uma maior capacidade dos veículos de entrega.

# 5.3 Entregas por Região
# Cria um DataFrame com a contagem normalizada das combinações de região e capacidade dos veículos, e retorna a proporção dessas combinações.

data = pd.DataFrame(deliveries_df[["region", "vehicle_capacity"]].value_counts(normalize=True)).reset_index()
data.rename(columns={"proportion": "region_percent"}, inplace=True)
data.head()

# Gera o gráfico com as proporções de entregas por região.

with sns.axes_style("whitegrid"):
  grafico = sns.barplot(data=data, x="region", y="region_percent", ci=None, palette="pastel")
  grafico.set(title="Proporção de entregas por região", xlabel="Região", ylabel="Proporção" + "(%)")

# Insights:
# Os hubs DF-1 e DF-2 possuem uma proporção significativamente maior de entregas em comparação com o DF-0. Embora a capacidade dos veículos seja a mesma para os três hubs, seria ideal alocar mais recursos para as regiões com maior demanda e priorizar maior agilidade. Por outro lado, o DF-0 prioriza a agilidade, visto que possui uma distribuição mais espalhada de entregas.