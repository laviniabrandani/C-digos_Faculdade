lista  = ["Roberto", "Souza", "Porto"]
if "Souza" in lista:            # Operador in usado para verificar se um conteúdo está contido na Lista.
    print("Positivo")

lista.append("kkkk")            # Método append() acrescenta um novo valor no fim da Lista.
print(lista)

lista.sort()                    # Método sort() ordena a Lista.
print(lista)

print("Contagem:", len(lista))  # Método len() retorna a quantidade de elementos da Lista.

print(lista.count("Porto"))     # Método count() retorna a quantidade de vezes que um valor aparece na Lista.

lista2 = lista.copy()           # Método copy() retorna uma cópia da Lista.
print(lista2)

lista.extend("teste")           # Método extend() acrescenta valores a uma Lista.
print(lista)

aux = [1, 2, 3]
lista.extend(aux)               # Método extend() acrescenta valores a uma Lista.
print(lista)

lista = lista + [4, 5, 6]       # O operador + acrescenta (concatena) uma Lista em outra Lista.
print(lista)

print(lista.index("Roberto"))   # Método index() retorna a posição de valor em uma Lista.

lista.insert(1, "de")           # Método insert() insere um valor em uma posição da Lista. 
print(lista)

print(lista.pop(0))             # Método pop() remove um valor de uma posição da Lista e retorna o valor.
print(lista)

lista.remove("kkkk")            # Método remove() um valor da Lista. Retorna erro caso não encontre.
print(lista)

lista.reverse()                 # Método reverse() inverte os valores de uma Lista.
print(lista)

lista.clear()                   # Método clear() apaga os valores de uma Lista. Limpa a Lista.
print(lista)
