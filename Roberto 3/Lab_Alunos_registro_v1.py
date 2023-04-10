from os import system

N = 3

lista = []  # Cria uma lista.

cont = 1
while cont <= N:
    system("cls")
    matricula = input("Matrícula do aluno: ")
    nome = input("Nome do aluno: ")
    disciplina = input("Disciplina: ")
    bim1 = int(input("Nota Bimestre 1: "))
    bim2 = int(input("Nota Bimestre 2: "))
    lista.append({"matricula": matricula, "nome": nome, "disciplina": disciplina, "bim1": bim1, "bim2": bim2})
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