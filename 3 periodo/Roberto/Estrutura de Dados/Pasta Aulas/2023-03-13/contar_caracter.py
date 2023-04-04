arq = open("texto.txt", "r")

caracteres = []
frequencia = []
carac = arq.read(1) # O método read(1) le apenas um caracter (1 byte) por vez.
while carac:
    if carac != "\n":
        try:
            pos  = caracteres.index(carac)
        except:
            caracteres.append(carac)
            frequencia.append(1)
        else:
            frequencia[pos] += 1
    carac = arq.read(1)

tam = len(frequencia)
i = 0
while i < tam:
    print(caracteres[i], frequencia[i])
    i += 1