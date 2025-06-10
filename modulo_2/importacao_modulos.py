# Importar módulos de um pacote
# Para utilizar um módulo em nosso programa, devemos importá-lo utilizando a declaração import. 
# Podemos importar um módulo completo ou funções específicas de um módulo.
import math

resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0

# Também podemos importar funções específicas de um módulo utilizando a sintaxe from módulo import função.
from math import sqrt

resultado = sqrt(25)
print(resultado)  # Imprime 5.0

# Funções e classes de módulos padrão
# A biblioteca padrão de Python oferece uma ampla gama de módulos com funções e classes úteis. 
# Alguns exemplos comuns incluem: Math, Random, Datetime, JSON, CSV, entre outros.

import random
import datetime

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime um número inteiro aleatório entre 1 e 10

data_atual = datetime.datetime.now()
print(data_atual)  # Imprime a data e hora atual