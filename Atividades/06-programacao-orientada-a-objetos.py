# Módulo | Python: Programação Orientada a Objetos
# Caderno de Exercícios

# Tópicos
# 1.Um pouco de teoria;
# 2.Classes;
# 3.Objetos;
# 4.Herança.

# 0. Preparação do ambiente
# Neste exercício vamos trabalhar com os arquivos de csv e texto definidos na pasta de arquivos.

# 1. Classe para ler arquivos de texto
# Crie a classe ArquivoTexto. Ela deve conter os seguintes atributos:
# self.arquivo: Atributo do tipo str com o nome do arquivo;
# self.conteudo: Atributo do tipo list onde cada elemento é uma linha do arquivo;
# A classe também deve conter o seguinte método:
# self.extrair_linha: Método que recebe como parâmetro o número da linha e retorna o seu conteúdo.

class ArquivoTexto(object):

  def __init__(self, arquivo: str):
    self.arquivo = arquivo
    self.conteudo = conteudo=[]

  def extrair_linha(self, numero_linha: int):
    with open(file=self.arquivo, mode='r', encoding='utf8') as arquivo:
      self.conteudo = arquivo.readlines()
      return self.conteudo[numero_linha-1].strip()

# Utilize o código abaixo para testar sua classe.

arquivo_texto = ArquivoTexto(arquivo='musica.txt')

numero_linha = 1
print(arquivo_texto.extrair_linha(numero_linha=numero_linha))

numero_linha = 10
print(arquivo_texto.extrair_linha(numero_linha=numero_linha))

# 2. Classe para ler arquivos de csv
# Crie a classe ArquivoCSV. Ela deve extender (herdar) a classe ArquivoTexto para reaproveitar os seus atributos (self.arquivo e self.conteudo) e método (self.extrair_linha). Além disso, adicione o seguinte atributo:
# self.colunas: Atributo do tipo list onde os elementos são os nome das colunas;
# A classe também deve conter o seguinte método:
# self.extrair_coluna_da_linha: Método que recebe como parâmetro o numero da linha e o indice da coluna e retorna o valor em questão.

class ArquivoCSV(ArquivoTexto):

  def __init__(self, arquivo: str):
    super().__init__(ArquivoTexto)
    self.arquivo = arquivo
    self.colunas = self.extrair_nome_colunas()

  def extrair_nome_colunas(self):
    cabecalho = []
    with open(file=self.arquivo, mode='r', encoding='utf8') as arquivo:
      self.conteudo = arquivo.readlines()
      cabecalho = self.conteudo[0].strip().split(sep=',')
      return cabecalho

  def extrair_nome_da_coluna(self, numero_coluna: int):
    cabecalho = self.conteudo[0].strip().split(sep=',')
    nome_colunas = []
    nome_colunas = cabecalho[numero_coluna-1]
    return nome_colunas

  def extrair_coluna_da_linha(self, numero_linha: int, numero_coluna: int):
    linha = self.extrair_linha(numero_linha).split(sep=',')
    return linha[numero_coluna-1]

# Utilize o código abaixo para testar sua classe.

arquivo_csv = ArquivoCSV(arquivo='carros.csv')

numero_linha = 1
print(arquivo_csv.extrair_linha(numero_linha=numero_linha))

print(arquivo_csv.colunas)

numero_linha = 10
print(arquivo_csv.extrair_linha(numero_linha=numero_linha))

numero_linha = 10
numero_coluna = 2
print(arquivo_csv.extrair_coluna_da_linha(numero_linha=numero_linha, numero_coluna=numero_coluna))