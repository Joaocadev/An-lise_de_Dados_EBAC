# Módulo | Python: Tratamento de Erros
# Caderno de Exercícios

# Tópicos
# 1.Tipos de erros;
# 2.Erros de sintaxe;
# 3.Erros em tempo de execução.

# 1. Erros de sintaxe
# Identifique o erro de sintaxe nos trechos de código abaixo e corrija-os para que o trecho de código funcione.

# Laços de repetição.

# Código original:
credito = {'123': 750, '456': 812, '789': 980}

for chave, valor in credito.items():
  print(f'Para o documento {chave}, o valor do escore de crédito é {valor}.")

# Código corrigido:
credito = {'123': 750, '456': 812, '789': 980}

for chave, valor in credito.items():
  print(f'Para o documento {chave}, o valor do escore de crédito é {valor}.')

# Funções

# Código original:
def pi() --> float:
  return 3.14159265359

pi = pi()
print(pi)

# Código corrigido:
def pi() -> float:
  return 3.14159265359

pi = pi()
print(pi)

# Programação Funcional

# Código original:
emails = ['andre.perez@gmail.com', 'andre.perez@live.com', 'andre.perez@yahoo.com']
provedor_da_google = lambda email: 'gmail in email

emails_google = filter(provedor_da_google, emails)
print(list(emails_google))

# Código corrigido:
emails = ['andre.perez@gmail.com', 'andre.perez@live.com', 'andre.perez@yahoo.com']
provedor_da_google = lambda email: 'gmail in email'

emails_google = filter(provedor_da_google, emails)
print(list(emails_google))

# Programação orientação a objetos

# Código original:
class Pessoa(object):

  def __init__(self nome: str, idade: int, documento: str):
    self.nome = nome
    self.idade = idade
    self.documento = documento

andre = Pessoa(nome="Andre", idade=30, document="123")

# Código corrigido:
class Pessoa(object):

  def __init__(self, nome: str, idade: int, documento: str):
    self.nome = nome
    self.idade = idade
    self.documento = documento

andre = Pessoa(nome="Andre", idade=30, documento="123")

# 2. Erros em tempo de execução
# Neste exercício vamos trabalhar com o arquivo csv com dados de crédito, definido na pasta de arquivos.

# O código abaixo deve calcular o total emprestado por cada vendedor mas está "estourando" a exceção ValueError devido a um erro no conjunto de dados. Utilize a estrutura try-catch para garantir que o código seja executado com sucesso.
# Atenção: Você não deve alterar o arquivo de dados.

# Código original:
def valor_total_emprestimo(valor: float, quantidade: int) -> float:
  return valor * quantidade

emprestimos = []

with open(file='./credito.csv', mode='r', encoding='utf8') as fp:
  fp.readline() # cabeçalho
  linha = fp.readline()
  while linha:
    linha_emprestimo = {}
    linha_elementos = linha.strip().split(sep=',')
    linha_emprestimo['id_vendedor'] = linha_elementos[0]
    linha_emprestimo['valor_emprestimos'] = float(linha_elementos[1])
    linha_emprestimo['quantidade_emprestimos'] = int(linha_elementos[2])
    linha_emprestimo['data'] = linha_elementos[3]
    emprestimos.append(linha_emprestimo)
    linha = fp.readline()

emprestimos_total = []
for emprestimo in emprestimos:
  valor_total = valor_total_emprestimo(valor=emprestimo['valor_emprestimos'], quantidade=emprestimo['quantidade_emprestimos'])
  emprestimos_total.append({emprestimo['id_vendedor']: valor_total})

for emprestimo_total in emprestimos_total:
  print(emprestimo_total)

# Código corrigido:
def valor_total_emprestimo(valor: float, quantidade: int) -> float:
  return valor * quantidade

emprestimos = []

with open(file='./credito.csv', mode='r', encoding='utf8') as fp:
  fp.readline() # cabeçalho
  linha = fp.readline()
  while linha:
    linha_emprestimo = {}
    linha_elementos = linha.strip().split(sep=',')
    linha_emprestimo['id_vendedor'] = linha_elementos[0]
    try:
      linha_emprestimo['valor_emprestimos'] = float(linha_elementos[1])
    except ValueError:
      linha_elementos[1] = linha_elementos[1].replace('"', '')
    finally:
      linha_emprestimo['valor_emprestimos'] = float(linha_elementos[1])
    linha_emprestimo['quantidade_emprestimos'] = int(linha_elementos[2])
    linha_emprestimo['data'] = linha_elementos[3]
    emprestimos.append(linha_emprestimo)
    linha = fp.readline()

emprestimos_total = []
for emprestimo in emprestimos:
  valor_total = valor_total_emprestimo(valor=emprestimo['valor_emprestimos'], quantidade=emprestimo['quantidade_emprestimos'])
  emprestimos_total.append({emprestimo['id_vendedor']: valor_total})

for emprestimo_total in emprestimos_total:
  print(emprestimo_total)

