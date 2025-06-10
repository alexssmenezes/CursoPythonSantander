ponto = (3,4)  # Cria uma tupla com os valores 3 e 4
# Imprime a tupla
# Acessa os elementos da tupla usando índices
print("Criada a tupla com os valores 3 e 4.", ponto)
print("Imprimindo o elemento na posição 0 na tupla =", ponto[0])
print("Imprimindo o elemento na posição 1 na tupla =", ponto[1]) 
# Tuplas são estruturas de dados imutáveis, ou seja, não podem ser alteradas após a criação.
# Imprime linha tracejada e pula linha antes e depois.

print("\n----------------------------------------------------\n")

print("count(elemento): devolve o número de vezes que um elemento aparece na tupla.")
print("index(elemento): devolve o índice da primeira aparição de um elemento na tupla.")
print("Opcionalmente, pode-se especificar o início e fim da busca.")
print("len(tupla): embora não seja um método de tupla propriamente dito, esta função incorporada devolve o comprimento da tupla.")

# Imprime linha tracejada e pula linha antes e depois.
print("\n----------------------------------------------------\n")

minha_tupla = (1, 2, 3, 2, 4, 2)
print("Tupla criada:", minha_tupla)
print("Tamanho da tupla:", len(minha_tupla))  # Saída: 6
print(minha_tupla.count(2))  # Saída: 3
print(minha_tupla.index(2)) # Saída: 1
print(minha_tupla.index(2, 2)) # Saída: 3
print(minha_tupla.index(2, 2, 4)) # Saída: 3
