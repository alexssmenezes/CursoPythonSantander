print("Para criar um conjunto, utilize chaves ou a função set():")
# Criando um conjunto com chaves
frutas = {"maçã", "banana", "laranja"}
numeros = set([1, 2, 3, 4, 5])

print("Os conjuntos suportam operações matemáticas de conjuntos, como a união (|), a interseção (&), a diferença (-) e a diferença simétrica (^).")
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

uniao = conjunto1 | conjunto2
print(uniao)  # Imprime {1, 2, 3, 4, 5}

intersecao = conjunto1 & conjunto2
print(intersecao)  # Imprime {3}

diferenca = conjunto1 - conjunto2
print(diferenca)  # Imprime {1, 2}

diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)  # Imprime {1, 2, 4, 5}

# Imprime linha tracejada e pula linha antes e depois.
print("\n----------------------------------------------------\n")

print("add(elemento): adiciona um elemento ao conjunto.")
print("remove(elemento): remove um elemento do conjunto. Se o elemento não existir, gera um erro.")
print("discard(elemento): remove um elemento do conjunto se estiver presente. Se o elemento não existir, não faz nada.")
print("clear(): remove todos os elementos do conjunto.")
frutas = {"maçã", "banana", "laranja"}

# Adicionando um elemento ao conjunto
frutas.add("pera")
print(frutas)  # Imprime {"maçã", "banana", "laranja", "pera"}

# Removendo um elemento do conjunto
frutas.remove("banana")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}

# Tentando remover um elemento que não existe gera um erro
frutas.discard("uva")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}

# Removendo um elemento que não existe sem gerar erro
frutas.clear()
print(frutas)  # Imprime set()