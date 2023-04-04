lista = ["Lavinia", "Rodrigues", "Brandani"]
if "Brandani" in lista:
    print('True')
else:
    print('False')

lista.append('Tenorio')
print(lista)

i = 0
while i < len(lista):   #printa os elementos da lista sem estar no formato 
    print(lista[i], end=" ")
    i += 1

# lista.sort()
# print(lista)

# print("Contagem", len(lista))  # Retorna quantidade de elementos da lista

# print(lista.count("Rodrigues"))

# lista2 = lista.copy()
# print(lista2)

# lista.extend("teste")
# print(lista)

# aux = [1,2,3]
# lista.extend(aux)
# print(lista)

# lista = lista + [4,5,6]
# print(lista)

# print(lista.index('Lavinia')) #Mostra a posição

# lista.insert(1,'de') #poe o elemento na posição que quer
# print(lista)

# print(lista.pop(0)) #retira o elemento da lista de acordo com a posição
# print(lista)

# lista.remove('Tenorio') #retira o valor espefícico
# print(lista)

# lista.reverse()
# print(lista)

# lista.clear()
# print(lista)