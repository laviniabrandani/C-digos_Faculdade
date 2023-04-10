
arq = open("disciplina.txt", "r")

# Lendo todas as linhas de um arquivo texto
print("Listando com WHILE")
linha = arq.readline()
while linha:
    print(linha.rstrip("\n"))
    linha = arq.readline()

# Ou assim   
print("Listando com FOR")
arq.seek(0) # Posiciona o ponteiro de arquivo (apontador) apontando para o Byte 0 (primeiro).
for linha in arq:
    print(linha.rstrip("\n"))

# Ou ainda lendo todas as linhas de uma só vez gerando uma lista de linhas
print("Listando utilizando LISTA")
arq.seek(0)
lista = arq.readlines()
for linha in lista:
    print(linha.rstrip("\n"))

arq.close()

