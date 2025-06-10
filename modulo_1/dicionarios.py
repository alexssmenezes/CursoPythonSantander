# Criando dicionários
pessoa = {'nome': 'Alex', 'idade': 45, 'cidade': 'Poá'}

# Acessando valores
print("Nome:", pessoa['nome'])  # Acessa o valor associado à chave 'nome'
print("Idade:", pessoa['idade'])  # Acessa o valor associado à chave 'idade'
print("Cidade:", pessoa['cidade'])  # Acessa o valor associado à chave 'cidade'

# Adicionando novos pares chave-valor
pessoa['profissão'] = 'Desenvolvedor'  # Adiciona a chave 'profissão' com o valor 'Desenvolvedor'
print("Profissão:", pessoa['profissão'])  # Acessa o valor associado à chave 'profissão'

# Atualizando valores
pessoa['idade'] = 46  # Atualiza o valor associado à chave 'idade'
print("Idade atualizada:", pessoa['idade'])  # Acessa o valor atualizado

# Removendo pares chave-valor
del pessoa['cidade']  # Remove a chave 'cidade' e seu valor associado
print("Dicionário após remoção da cidade:", pessoa)  # Imprime o dicionário atualizado

# Verificando se uma chave existe
if 'nome' in pessoa:  # Verifica se a chave 'nome' existe no dicionário
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")

# Imprime linha tracejada e pula linha antes e depois.
print("\n----------------------------------------------------\n")

# Criando outro dicionário
pessoa2 = {"nome": "Sandro", "idade": 35, "cidade": "Suzano"}

print(pessoa2.keys())    # Imprime dict_keys(["nome", "idade", "cidade"])
print(pessoa2.values())  # Imprime dict_values(["Sandro", 35, "Suzano"])
print(pessoa2.items())   # Imprime dict_items([("nome", "Sandro"), ("idade", 35), ("cidade", "Suzano")])

# Atualizando o dicionário
pessoa2.update({"profissao": "Designer"})
print(pessoa2)  # Imprime {"nome": "Sandro", "idade": 35, "cidade": "Suzano", "profissao": "Designer"}