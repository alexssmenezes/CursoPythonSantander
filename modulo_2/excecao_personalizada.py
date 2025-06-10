""""
Para criar uma exceção personalizada, você deve criar uma classe 
que herde da classe base Exception ou de uma de suas subclasses.
"""

def funcao():
    # Código que pode gerar uma exceção personalizada
    condicao = True  # Defina a condição conforme necessário
    if condicao:
        raise Exception("Descrição do erro")

try:
    funcao()
except Exception as e:
    print(f"Erro: {str(e)}")