string = input("String: ")
tam = len(string)
letras = []
i = 0
while i < tam:
    res = string.count((string[i]))
    if not string[i] in letras:
        print(string[i], res)
        letras.append(string[i])
    i += 1