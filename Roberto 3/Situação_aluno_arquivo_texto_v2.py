
arq = open("disciplina.txt", "r")
arq_saida = open("Situacao_aluno.txt", "w")

for linha in arq:
    lista = linha.rstrip("\n").split()
    media = (int(lista[1]) + int(lista[2])) / 2
    if media >= 70.0:
        situacao = "Aprovado"
    elif media >= 30.0:
        situacao = "Em Exame"
    else:
        situacao = "Reprovado"
    saida = linha.rstrip("\n") + " " + str(media) + " " + situacao + "\n"
    arq_saida.write(saida)

arq.close()
arq_saida.close()

