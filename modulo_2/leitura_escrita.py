# Leitura de arquivos
"""Para ler o conteúdo de um arquivo, primeiro devemos abri-lo 
utilizando a função open() em modo de leitura ("r"). Depois, 
podemos ler o conteúdo do arquivo utilizando métodos como read() ou readlines().
"""
arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

# Escrita de arquivos
"""Para escrever dados em um arquivo, abrimos em modo de escrita ("w")
utilizando a função open(). Se o arquivo não existir, será criado automaticamente. 
Se o arquivo já existir, seu conteúdo será sobrescrito.
"""
arquivo = open("dados.txt", "w")
arquivo.write("Olá, mundo!")
arquivo.close()

# Você também pode utilizar a declaração with para manejar a abertura e fechamento de arquivos de maneira automática.
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)