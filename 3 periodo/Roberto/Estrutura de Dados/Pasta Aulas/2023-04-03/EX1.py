print("#" * 30, "teste 1", "#" * 30)
reg = {"matricula": "", "nome": ""}
reg["matricula"] = 100
reg["nome"] = "Lavinia Brandani"
print(reg)

# reg["matricula"] = input("Digite a matrícula: ")
# reg["nome"] = input("Digite o nome: ")
# print(reg)
##############################################################################
print("#" * 30, "teste 2", "#" * 30)
print(reg["matricula"], reg["nome"])
print(reg.get("matricula")) #outra forma de usar
print(reg.get("nota", "Dado inexistente")) #outra forma de usar

##############################################################################
print("#" * 30, "teste 3", "#" * 30)
print("for chave in reg: ")
for chave in reg:
    print(chave, reg[chave])

##############################################################################
print("#" * 30, "teste 4", "#" * 30)
for tupla in reg.items():
    print(tupla[0], tupla[1])

##############################################################################
print("#" * 30, "teste 5", "#" * 30)
for chave, valor in reg.items():
    print(chave, valor)

##############################################################################
print("#" * 30, "teste 6", "#" * 30)
for valor in reg.values():
    print(valor)

##############################################################################
print("#" * 30, "teste 7", "#" * 30)
reg["cidade"] = "Santa Rita do Sapucai"
print(reg)

##############################################################################
print("#" * 30, "teste 8", "#" * 30)
lista = reg.keys()
print(lista)

##############################################################################
print("#" * 30, "teste 9", "#" * 30)
lista = reg.values()
print(lista)

##############################################################################
print("#" * 30, "teste 10", "#" * 30)
lista = reg.items()
print (lista)

##############################################################################
print("#" * 30, "teste 11", "#" * 30)
if "nome" in reg:
    print("Chave nome existe")

##############################################################################
print("#" * 30, "teste 12", "#" * 30)
if 100 in reg.values():
    print("O valor 100 existe")

##############################################################################
print("#" * 30, "teste 13", "#" * 30)
del reg["cidade"]
print(reg)

##############################################################################
print("#" * 30, "teste 14", "#" * 30)
nome = reg.pop("nome")
print(nome)
print(reg)

##############################################################################
print("#" * 30, "teste 15", "#" * 30)
copia = reg.copy()
print(reg, copia)

##############################################################################
print("#" * 30, "teste 16", "#" * 30)
reg.clear()
print(reg)