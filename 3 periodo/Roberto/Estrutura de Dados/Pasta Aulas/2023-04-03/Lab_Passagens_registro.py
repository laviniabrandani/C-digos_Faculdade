
Bilhetes = []

def ModuloPrincipal():
    Opcao = 0

    while Opcao != 6:
        print("    FICHA DE BILHETES    ")
        print("==========================")
        print("1 - Cadastro de passagem")
        print("2 - Pesquisa da idade média dos passageiros")
        print("3 - Pesquisa da idade média dos passageiros por horário de embarque")
        print("4 - Relatório de passageiros por destino e data de embarque")
        print("5 - Pesquisa por número de passagem")
        print("6 - Sair")
        Opcao = int(input("Opção: "))
        if Opcao == 1:
            Cadastro(Bilhetes)
        else:
            if Opcao == 2:
                IdadeMedia(Bilhetes)
            else:
                if Opcao == 3:
                    Horario = input("Horário de Embarque: ")
                    IdadeMediaPorEmbarque(Bilhetes, Horario)
                else:
                    if Opcao == 4:
                        Destino = input("Cidade de Destino: ")
                        Horario = input("Horário de Embarque: ")
                        RelatorioDestinoEmbarque(Bilhetes, Destino, Horario)
                    else:
                        if Opcao == 5:
                            Passagem = input("Número da passagem: ")
                            PesquisaPassagem(Bilhetes, Passagem)
                        else:
                            if Opcao == 6:
                                print("Finalizando.....")
                            else:
                                print("Opção Inválida")


def Cadastro(Bilhetes):
    i = len(Bilhetes)
    Bilhetes.append({"passsagem": "", "data": "", "origem": "", "destino": "", "horario": "", "poltrona": "", "idade": "", "nome": ""})
    Bilhetes[i]["passagem"] = input("Número da passagem: ")
    Bilhetes[i]["data"] = input("Data: ")
    Bilhetes[i]["origem"] = input("Origem: ")
    Bilhetes[i]["destino"] = input("Destino: ")
    Bilhetes[i]["horario"] = input("Horário: ")
    Bilhetes[i]["poltrona"] = input("Poltrona: ")
    Bilhetes[i]["idade"] = input("Idade: ")
    Bilhetes[i]["nome"] = input("Nome do passageiro: ")

def IdadeMedia(Bilhetes):
    Tam = len(Bilhetes)
    IdadeM = 0
    i = 0
    while i < Tam:
        IdadeM = Bilhetes[i]["idade"] + IdadeM
        i += 1
    IdadeM = IdadeM / Tam
    return IdadeM

def IdadeMediaPorEmbarque(Bilhetes, Horario):
    Tam = len(Bilhetes)
    IdadeMEmbarque = 0
    i = 0
    while i < Tam:
        if Horario == Bilhetes[i]["destino"]:
            IdadeMEmbarque = Bilhetes[i]["idade"] + IdadeMEmbarque
            i += 1
    IdadeMediaFinal = IdadeMEmbarque / Tam
    return IdadeMediaFinal

def RelatorioDestinoEmbarque(Bilhetes, Destino, Horario):
    Tam = len(Bilhetes)
    i = 0
    while i < Tam:
        if Bilhetes[i]["destino"] == Destino and Bilhetes[i]["horario"] == Horario:
            print(Bilhetes[i]["nome"])
            print(Bilhetes[i]["data"])
        i += 1

def PesquisaPassagem(Bilhetes, Passagem):
    Tam = len(Bilhetes)
    i = 0
    while i < Tam and Bilhetes[i]["passagem"] != Passagem:
        i += 1
    if i < Tam:
        print(Bilhetes[i]["passagem"])
        print(Bilhetes[i]["data"])
        print(Bilhetes[i]["origem"])
        print(Bilhetes[i]["destino"])
        print(Bilhetes[i]["horario"])
        print(Bilhetes[i]["poltrona"])
        print(Bilhetes[i]["idade"])
        print(Bilhetes[i]["nome"])
    else:
        print("Passagem não encontrada!")

ModuloPrincipal()