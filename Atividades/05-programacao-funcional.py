# Módulo | Python: Programação Funcional
# Caderno de Exercícios

# Tópicos
# 1.Função lambda;
# 2.Função map;
# 3.Função filter;
# 4.Função reduce.

# 0. Preparação do ambiente
# Neste exercício vamos trabalhar com o arquivo csv com dados de crédito.

# Vamos ler o conteúdo do arquivo em uma lista onde cada elemento é um dicionário representando as linhas do arquivo.

emprestimos = []
with open(file='./credito.csv', mode='r', encoding='utf8') as fp:
  fp.readline() # cabeçalho
  linha = fp.readline()
  while linha:
    linha_emprestimo = {}
    linha_elementos = linha.strip().split(sep=',')
    linha_emprestimo['id_vendedor'] = linha_elementos[0]
    linha_emprestimo['valor_emprestimos'] = linha_elementos[1]
    linha_emprestimo['quantidade_emprestimos'] = linha_elementos[2]
    linha_emprestimo['data'] = linha_elementos[3]
    emprestimos.append(linha_emprestimo)
    linha = fp.readline()

for emprestimo in emprestimos:
  print(emprestimo)

# 1. Função map
# Aplique a função map na lista de emprestimos para extrair os valores da chave valor_emprestimos na lista valor_emprestimos_lista. Faça também a conversão de str para float.

valor_emprestimos_lista = list(map(lambda val: float(val['valor_emprestimos']), emprestimos))

print(valor_emprestimos_lista)

# 2. Função filter
# Aplique a função filter na lista de valor_emprestimos_lista para filtrar apenas os valores maiores que zero (os valores negativas são erros na base de dados). Salve os valores na lista valor_emprestimos_lista_filtrada.

valor_emprestimos_lista_filtrada = list(filter(lambda val: val > 0, valor_emprestimos_lista))

print(valor_emprestimos_lista_filtrada)

# 3. Função reduce para extrair a soma
# Aplique a função reduce para somar os elementos da lista valor_emprestimos_lista_filtrada na variavel soma_valor_emprestimos.

from functools import reduce

soma_valor_emprestimos = (reduce(lambda x, y: x + y, valor_emprestimos_lista_filtrada))

print(soma_valor_emprestimos)

# 3.1. Função reduce para extrair a media aritimética
# Aplique a função reduce para extrair a média aritimética dos elementos da lista valor_emprestimos_lista_filtrada na variavel media_valor_emprestimos.
# Dica: Para calcular o tamanho da lista, isto é a quantidade de elementos, utilize a função len(), dentro do argumento da função coloque a lista valor_emprestimos_lista_filtrada.

from functools import reduce

soma = reduce(lambda x, y: x + y, valor_emprestimos_lista_filtrada)
media_valor_emprestimos = soma / len(valor_emprestimos_lista_filtrada)

print(media_valor_emprestimos)

# 3.2. (Desafio) Função reduce para extrair o desvio padrão amostral
# Aplique a função reduce para extrair a média aritimética dos elementos da lista valor_emprestimos_lista_filtrada na variavel desvio_padrao_valor_emprestimos.

from functools import reduce
import math

soma = reduce(lambda x, y: x + y, valor_emprestimos_lista_filtrada)
media_valor_emprestimos = soma / len(valor_emprestimos_lista_filtrada)
media_ao_quadrado = list(map(lambda x: (x - media_valor_emprestimos) ** 2, valor_emprestimos_lista_filtrada))
media_dos_quadrados = reduce(lambda x, y: x + y, media_ao_quadrado) / (len(valor_emprestimos_lista_filtrada) - 1)
desvio_padrao_valor_emprestimos = math.sqrt(media_dos_quadrados)

print(desvio_padrao_valor_emprestimos)