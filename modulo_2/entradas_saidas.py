# Entrada de dados do usuário
nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")

print("Olá, " + nome + "!")
print("Você tem " + idade + " anos.")


idade2 = int(input("Insira sua idade: "))

if idade2 >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
    
# Saída de dados formatada
# Podemos utilizar a f-string (formatação de cadeias) para inserir variáveis diretamente dentro de uma cadeia de texto.
nome2 = "Juan"
idade3 = 25

print(f"Olá, meu nome é {nome2} e tenho {idade3} anos.")