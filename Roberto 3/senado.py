
arq = open("senado.txt", "r")
arq_saida = open("apuracao_senado.txt", "w")
cont1 = cont2 = cont3 = cont4 = 0
string1 = string2 = string3 = ""
for linha in arq:
    lista = linha.rstrip("\n").split()
    if lista[1] == "1":
        cont1 += 1
        string1 += lista[0] + ", " 
    elif lista[1] == "2":
        cont2 += 1
        string2 += lista[0] + ", "
    elif lista[1] == "3":
        cont3 += 1
        string3 += lista[0] + ", "
    else:
        cont4 += 1
string1 += "\n"
string2 += "\n"
string3 += "\n"
total_votos = cont1 + cont2 + cont3 + cont4
arq_saida.write("ELEICAO - PRESIDENCIA DO SENADO \n")
arq_saida.write("=============================== \n")
arq_saida.write("Candidato 1 = " + str(cont1) + " voto(s), " + str(cont1/total_votos*100) + "%" + "\n")
arq_saida.write("Candidato 2 = " + str(cont2) + " voto(s), " + str(cont2/total_votos*100) + "%" + "\n")
arq_saida.write("Candidato 3 = " + str(cont3) + " voto(s), " + str(cont3/total_votos*100) + "%" + "\n")
arq_saida.write("Nulos/Brancos = " + str(cont4) + " voto(s), " + str(cont4/total_votos*100) + "%" + "\n")
arq_saida.write("=============================== \n")
arq_saida.write("Eleitores do Candidato 1: " + string1)
arq_saida.write("Eleitores do Candidato 2: " + string2)
arq_saida.write("Eleitores do Candidato 1: " + string3)
arq.close()
arq_saida.close()

