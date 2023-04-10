from os import system

def Menu():
    lista = []
    opcao = 0
    while opcao != 6:
        system("cls")
        print("            AGENDA DE CONTATOS            ")
        print("==========================================")
        print("Opção 1 - Incluir Contato")
        print("Opção 2 - Consultar Contato")
        print("Opção 3 - Editar Contato")
        print("Opção 4 - Excluir Contato")
        print("Opção 5 - Mostrar Agenda")
        print("Opção 6 - Sair da Agenda")
        opcao = int(input("Opção: "))
        if opcao == 1:
            Inclusao(lista)
        elif opcao == 2:
            Consulta(lista)
            system("pause")
        elif opcao == 3:
            Alteracao(lista)
            system("pause")
        elif opcao == 4:
            Exclusao(lista)
            system("pause")
        elif opcao == 5:
            Listagem(lista)
            system("pause")
        elif opcao == 6:
            print("Finalizando...")
        else:
            print("Opção inváida")

def Inclusao(lista):
    system("cls")
    contato = input("Contato: ")
    numero = int(input("Número: "))
    lista.append({"nome" : contato, "numero" : numero})

def Consulta(lista):
    system("cls")
    contato = input("Nome do contato: ")
    tam = len(lista)
    i = 0
    while i < tam and lista[i]["nome"] != contato:
        i += 1
    if i < tam:
        print(f"Nome: {lista[i]['nome']}")   
        print(f"Número: {lista[i]['numero']}")
    else:
        print("Contato não encontrado")

def Alteracao(lista):
    system("cls")
    contato = input("Nome do contato: ")
    tam = len(lista)
    i = 0
    while i < tam and lista[i]["nome"] != contato:
        i += 1
    if i < tam:
        print(f"Nome: {lista[i]['nome']}")   
        print(f"Número: {lista[i]['numero']}")
        print()
        print("Qual alteração você deseja realizar?")
        print("Opção 1 - Alterar Nome")
        print("Opção 2 - Alterar Número")
        opcao = int(input("Opção escolhida: "))
        if opcao == 1:
            lista[i]["nome"] = input("Nome: ")
        elif opcao == 2:
            lista[i]["numero"] = int(input("Número: "))
        print("Alteração concluida com sucesso!")
    else:
        print("Contato não encontrado")

def Exclusao(lista):
    system("cls")
    contato = input("Nome do contato: ")
    tam = len(lista)
    i = 0
    while i < tam and lista[i]["nome"] != contato:
        i += 1
    if i < tam:
        print(f"Nome: {lista[i]['nome']}")   
        print(f"Número: {lista[i]['numero']}")
        print()
        opcao = input("Deseja realmente excluir (S/N)?: ")
        if opcao == "S" or opcao == "s":
            del(lista[i])
            print("O contato foi excluído com sucesso!")
    else:
        print("Contato não encontrado")

def Listagem(lista):
    system("cls")
    for reg in lista:
        print("Nome: ", reg["nome"])
        print("Número: ", reg["numero"])
        print()

Menu()