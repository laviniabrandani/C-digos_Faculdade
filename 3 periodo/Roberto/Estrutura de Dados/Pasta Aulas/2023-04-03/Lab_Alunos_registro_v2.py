from os import system

N = 3

lista = []  # Cria uma lista vazia.

cont = 1
while cont <= N:
    system("cls")
    dic = {"matricula":"", "nome":"", "disciplina":"", "bim1":"", "bim2":""}
    dic["matricula"] = input("Matrícula do aluno: ")
    dic["nome"] = input("Nome do aluno: ")
    dic["disciplina"] = input("Disciplina: ")
    dic["bim1"] = int(input("Nota Bimestre 1: "))
    dic["bim2"] = int(input("Nota Bimestre 2: "))
    lista.append(dic)
    cont += 1

system("cls")
for reg in lista:
    media = (reg["bim1"] + reg["bim2"]) / 2
    print(reg["matricula"], reg["nome"], reg["disciplina"], reg["bim1"], reg["bim2"], media, end=" ")
    if media >= 70:
        print("Aprovado")
    elif media >= 30:
        print("Exame")
    else:
        print("Reprovado")
system("pause")