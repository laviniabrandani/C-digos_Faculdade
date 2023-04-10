
arq = open("disciplina.txt", "r")

for linha in arq:
    lista = linha.rstrip("\n").split()
    media = (int(lista[1]) + int(lista[2])) / 2
    if media >= 70.0:
        situacao = "Aprovado"
    elif media >= 30.0:
        situacao = "Em Exame"
    else:
        situacao = "Reprovado"
    print(lista[0], lista[1], lista[2], media, situacao)

arq.close()

