# Módulo | Python: Arquivos & Funções
# Caderno de Exercícios

# Tópicos
# 1.Leitura;
# 2.Escrita;
# 3.Funções;
# 4.Escopo.

# 1. Extração de coluna de arquivo csv
# 1.1. Extraia os valores valor_venda e armazena em uma lista.

valor_vendas = []

with open(file='./carros.csv', mode='r', encoding='utf8') as arquivo:
    linha = arquivo.readline() # lê o cabeçalho
    linha = arquivo.readline() # lê a primeira linha
    while linha:
      linha_separada = linha.split(sep=',') # quebra a string nas virgulas e salva os resultados em uma lista
      valor_venda = linha_separada[1] # seleciona o segundo elemento da lista
      valor_vendas.append(valor_venda) # salva o valor na lista de valor_venda
      linha = arquivo.readline() # lê uma nova linha, se a linha não existir, salva o valor None

print(valor_vendas)

# 1.2 Complete a função abaixo para extrair uma coluna, do arquivo csv em uma lista.

def extrai_coluna_csv(nome_arquivo: str, indice_coluna: int):

  coluna = []

  with open(file=nome_arquivo, mode='r', encoding='utf8') as arquivo: # leia o arquivo com o comando 'with' utilizando o parametro 'nome_arquivo'
    linha = arquivo.readline()
    linha = arquivo.readline()
    
    while linha: 
      linha_separada = linha.split(sep=',')
      indice = linha_separada[indice_coluna] # extraia a coluna do arquivo utilizando o parametro 'indice_coluna'
      coluna.append(indice)    
      linha = arquivo.readline()  
    
  return coluna

# Você pode testar a função com os códigos abaixo.

valor_manutencao = extrai_coluna_csv(nome_arquivo='./carros.csv', indice_coluna=2)
print(valor_manutencao)

porta_malas = extrai_coluna_csv(nome_arquivo='./carros.csv', indice_coluna=5)
print(porta_malas)

# Exercício bônus

# 1. Funções para arquivo csv
# Complete a função abaixo para extrair uma coluna do arquivo csv em uma lista. Os elementos devem ter o tipo de dado correto.

def extrai_coluna_csv(nome_arquivo: str, indice_coluna: int, tipo_dado: str):

  coluna = []

  # leia o arquivo com o comando 'with' utilizando o parametro 'nome_arquivo'
  with open(file=nome_arquivo, mode='r', encoding='utf8') as arquivo:
    linha = arquivo.readline()
    linha = arquivo.readline()
    while linha:
      linha_separada = linha.split(sep=',')
  # extraia a coluna do arquivo utilizando o parametro 'indice_coluna'
      indice = linha_separada[indice_coluna] 
  # use a estrutura de decisão if/elif/else para fazer a conversão do tipo de dados utilizando o parametro 'tipo_dado'      
      if tipo_dado == 'str': 
        str(indice)
      elif tipo_dado == 'int':
        int(indice)
      elif tipo_dado == 'float':
        float(indice)
      else:
        bool(indice)
      coluna.append(indice)
      linha = arquivo.readline()  
    
  return coluna

# Você pode testar a função com os códigos abaixo.

valor_venda = extrai_coluna_csv(nome_arquivo='./carros.csv', indice_coluna=1, tipo_dado='str')
print(valor_venda)

pessoas = extrai_coluna_csv(nome_arquivo='./carros.csv', indice_coluna=4, tipo_dado='int')
print(pessoas)

# 2. Funções para arquivo txt
# Complete a função abaixo para extrair uma as palavras de uma linha do arquivo txt em uma lista.

def extrai_linha_txt(nome_arquivo: str, numero_linha: int):

  palavras_linha = []

  # leia o arquivo com o comando 'with' utilizando o parametro 'nome_arquivo'
  with open(file=nome_arquivo, mode='r', encoding='utf8') as arquivo:
  # extraia a linha do arquivo utilizando o parametro 'numero_linha' 
    linha = arquivo.readlines()[numero_linha - 1]
  # quebre a linha em palavras com o comando split, note que o separador é um espaço ' '
    linha_separada = linha.split(sep=' ')
    palavras_linha.append(linha_separada)
    
  return palavras_linha

# Você pode testar a função com os códigos abaixo.

linha10 = extrai_linha_txt(nome_arquivo='./musica.txt', numero_linha=10)
print(linha10)