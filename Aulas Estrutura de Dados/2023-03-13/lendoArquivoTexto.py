arq = open("diciplina.txt", "r") #o arq já tem que existir como está lendo

#Lendo todas as linhas de um arquivo texto
print("Listando com WHILE")
linha = arq.readline()
while linha:  #enquanto a linha tiver algo é verdadeiro, quando for vazia da falso e para a repetição
    print(linha.rstrip("/n")) #exclui caracter da direita
    linha = arq.readline()

#Ou assim
print("Listando com FOR")
arq.seek(0) #Posiciona o ponteiro do arquivo (apontador) apontando para o
for linhda in arq:
    print(linha.strip("/n"))

#Ou aimda lendo todas as linhas de uma só vez gerando uma lista de linhas
print("Listando utilizando LISTA")
arq.seek(0)