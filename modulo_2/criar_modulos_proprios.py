# Criar e utilizar módulos personalizados
"""
Para criar um módulo personalizado, simplesmente criamos um novo arquivo Python
com o nome desejado e definimos as funções, classes e variáveis que queremos incluir no módulo. 
Por exemplo, criamos um arquivo (no mesmo diretório onde estamos executando Python) 
chamado meu_modulo.py com o seguinte conteúdo:
"""
#meu_modulo.py
def saudar(nome):
    print(f"Olá, {nome}!")

def calcular_soma(a, b):
    return a + b

# Depois, podemos importar e utilizar as funções definidas em meu_modulo.py em outro arquivo Python.
# import meu_modulo

# meu_modulo.saudar("João")  # Imprime "Olá, João!"
# resultado = meu_modulo.calcular_soma(5, 3)
# print(resultado)  # Imprime 8

# Organização do código em módulos
# podemos ter um módulo operacoes.py que contenha funções relacionadas com operações matemáticas,
# e outro módulo utilidades.py que contenha funções de uso geral.
# operacoes.py
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

# utilidades.py
def imprimir_mensagem(mensagem):
    print(mensagem)

def obter_nome_usuario():
    return input("Digite seu nome: ")

# Depois, podemos importar e utilizar essas funções em nosso programa principal.
"""
import operacoes
import utilidades

resultado = operacoes.somar(5, 3)
utilidades.imprimir_mensagem(f"O resultado da soma é: {resultado}")

nome = utilidades.obter_nome_usuario()
utilidades.imprimir_mensagem(f"Olá, {nome}!")
"""