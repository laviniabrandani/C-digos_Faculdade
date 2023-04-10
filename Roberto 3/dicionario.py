##############################################################
print("#" * 30, "TESTE 1", "#" * 30)
reg = {"matricula": "", "nome": ""} # Dicionário = registro
# Outra maneira: reg = dict(matricula="", nome="")
# Outra maneira: reg = dict(zip(["matricula", "nome"], ["", ""]))
# Outra maneira: reg = dict([("matricula", ""), ("nome", "")])

reg["matricula"] = 100  # reg.matricula = 100
reg["nome"] = "Roberto Porto" # reg.nome = "Roberto Porto"
print(reg)

##############################################################
print("#" * 30, "TESTE 2", "#" * 30)
print(reg["matricula"], reg["nome"])
print(reg.get("matricula")) # Faz a mesma coisa, porém permite uma msg de erro caso não encontre
print(reg.get("nota", "Dado inexistente"))

##############################################################
print("#" * 30, "TESTE 3", "#" * 30)
print("for chave in reg:")
for chave in reg: # A cada iteração retorna uma chave
    print(chave, reg[chave])

for tupla in reg.items(): # A cada iteração retorna uma Tupla com a chave/valor 
    print(tupla[0], tupla[1])

for chave, valor in reg.items(): #  A cada iteração retorna uma Tupla com os dados separados
    print(chave, valor)

for valor in reg.values(): # A cada iteração retorna um valor
    print(valor)

##############################################################
print("#" * 30, "TESTE 4", "#" * 30)
reg["cidade"] = "Santa Rita do Sapucaí" # Acrescenta um novo par (chave/valor) quando não existe
print(reg)                              # O mesmo que reg.update({"cidade": "Santa Rita do Sapucaí"})

##############################################################
print("#" * 30, "TESTE 5", "#" * 30)
lista = reg.keys() # Retorna uma *lista com as chaves 
print(lista) 

##############################################################
print("#" * 30, "TESTE 6", "#" * 30)
lista = reg.values() # Retorna uma *lista com os valores
print(lista) 

##############################################################
print("#" * 30, "TESTE 7", "#" * 30)
lista = reg.items() # Retorna uma *lista de tuplas com chave e valor
print(lista) 

##############################################################
print("#" * 30, "TESTE 8", "#" * 30)
if "nome" in reg:
    print("Chave nome existe")

##############################################################
print("#" * 30, "TESTE 9", "#" * 30)
if 100 in reg.values():
    print("Valor 100 existe")

##############################################################
print("#" * 30, "TESTE 10", "#" * 30)
del reg["cidade"] # Deleta (exclui) o par chave/valor
print(reg)

##############################################################
print("#" * 30, "TESTE 11", "#" * 30)
nome = reg.pop("nome") # Deleta (exclui) o par chave/valor e retorna o valor
print(nome)
print(reg)

##############################################################
print("#" * 30, "TESTE 12", "#" * 30)
copia = reg.copy() # Copiando um dicionário
print(reg, copia)

##############################################################
print("#" * 30, "TESTE 13", "#" * 30)
reg.clear() # Apaga o dicionário
print(reg)