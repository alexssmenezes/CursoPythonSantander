# Listas em Python
# Definindo uma lista de frutas
frutas = ["maçã", "banana", "laranja", "uva", "abacaxi"]

print("-- Imprimindo a lista.")
# Acessando elementos da lista
print(frutas[0])  # Imprime na tela o primeiro elemento -> maçã
print(frutas[1])  # Imprime na tela o segundo elemento da lista -> banana
print(frutas[2])  # Imprime na tela o terceiro elemento da lista -> laranja
print(frutas[3])  # Imprime na tela o quarto elemento da lista -> uva
print(frutas[4])  # Imprime na tela o quinto elemento da lista -> abacaxi

# Imprime linha tracejada e pula linha antes e depois.
print("\n----------------------------------------------------\n")

# Acessando elementos da lista usando índices negativos
print("-- Imprimindo a lista na ordem inversa.")
print(frutas[-1])  # Imprime na tela o primeiro elemento -> maçã
print(frutas[-2])  # Imprime na tela o segundo elemento da lista -> banana
print(frutas[-3])  # Imprime na tela o terceiro elemento da lista -> laranja
print(frutas[-4])  # Imprime na tela o quarto elemento da lista -> uva
print(frutas[-5])  # Imprime na tela o quinto elemento da lista -> abacaxi

# Imprime linha tracejada e pula linha antes e depois.
print("\n----------------------------------------------------\n")

# Verificando o tamanho da lista
print("-- (append): Inserindo a fruta kiwi ao final da lista.")
frutas.append("kiwi")  # Adiciona "kiwi" ao final da lista
print(frutas)  # Imprime a lista atualizada

# Imprime linha tracejada e pula linha antes e depois.
print("\n----------------------------------------------------\n")

# Inserindo uma nova fruta na primeira posição
print("-- (insert): Inserindo a fruta morango na posição 0 (zero).")
frutas.insert(0, "morango")  # Insere "morango" na primeira posição
print(frutas)  # Imprime a lista atualizada

# Imprime linha tracejada e pula linha antes e depois.
print("\n----------------------------------------------------\n")

# Removendo uma fruta da lista
print("-- (remove): Removendo a fruta banana da lista.")
frutas.remove("banana")  # Remove "banana" da lista
print(frutas)  # Imprime a lista atualizada

# Imprime linha tracejada e pula linha antes e depois.
print("\n----------------------------------------------------\n")

fruta_removida = frutas.pop(2)  # Remove e retorna o elemento da lista
print("-- (pop): Removendo a fruta da posição 2 da lista.")
print("A fruta removida foi", fruta_removida)  # Imprime a fruta removida
print("Lista atualizada: ", frutas)  # Imprime a lista atualizada

# Imprime linha tracejada e pula linha antes e depois.
print("\n----------------------------------------------------\n")

# Ordena a lista em ordem alfabética
frutas.sort()  
print("-- (sort): Ordenando a lista em ordem alfabética.")
print("Lista ordenada: ", frutas)  # Imprime a lista ordenada

# Imprime linha tracejada e pula linha antes e depois.
print("\n----------------------------------------------------\n")

# Inverte a ordem da lista
print("-- (reverse): Invertendo a ordem da lista.")
frutas.reverse()
print("Lista invertida: ", frutas)  # Imprime a lista invertida

# Imprime linha tracejada e pula linha antes e depois.
print("\n----------------------------------------------------\n")

print("A expressão x ** 2 eleva cada elemento ao quadrado, e a condição if x % 2 == 0 filtra apenas os números pares.")
print("Quadrados dos números pares da lista números:")
números = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in números if x % 2 == 0]
print("A lista exemplo é", números)  # Imprime a lista original
print("O resultado dos números pares elevados ao quadrado é", quadrados)  # Imprime [4, 16]

# Imprime linha tracejada e pula linha antes e depois.
print("\n----------------------------------------------------\n")
