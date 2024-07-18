# Módulo | Python: Variáveis & Tipos de Dados
# Caderno de Exercícios

# Tópicos
# 1.Introdução ao Google Colab;
# 2.Variáveis;
# 3.Números;
# 4.Strings;
# 5.Boleanos.

# 1. Google Colab
# Crie uma célula de código que escreva o texto "Olá mundo!", utilize o comando print.

print("Olá, mundo!")

# 2. Números
# Preencha as células de código para preencher os valores de (A), (B) e (C) na tabela de ticket médio.

# (A)
quantidade_total_vendas = 3
ticket_medio = 320.52

valor_total_vendas = quantidade_total_vendas * ticket_medio
print(valor_total_vendas)

# (B)
valor_total_vendas = 834.47
ticket_medio = 119.21

quantidade_total_vendas = valor_total_vendas / ticket_medio
print(int(quantidade_total_vendas))

# (C)
valor_total_vendas = 15378.12
quantidade_total_vendas = 5

ticket_medio = valor_total_vendas / quantidade_total_vendas
print(ticket_medio)

# 3. Strings
# Aplique três métodos distintos na string abaixo:

cancao = 'Roda mundo, roda gigante, roda moinho, roda pião.'

print(cancao.upper())

print(cancao.index("gigante"))

print(cancao.title())

# Extraia da string abaixo o valor da taxa selic na variável selic e o valor do ano na variavel ano. Imprima os valores na tela.

noticia = 'Selic vai a 2,75% e supera expectativas; é a primeira alta em 6 anos.'

posicao = noticia.find("2,75%")
print(posicao)

print(noticia[12:17])

posicao = noticia.find("6")
print(posicao)

# 4. Booleanos
# Utilize a tabela da verdade para responder: qual o valor da variável x?

a = False
b = True

x = not a & b

print(x)