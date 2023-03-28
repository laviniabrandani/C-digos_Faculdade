alunos = open("alunos.txt", "w")
nome = "Lavinia" + "\n"
nome1 = "Michele" + "\n"
alunos.write(nome + nome1)
alunos.close()

alunos = open("alunos.txt", "r")
string = alunos.read()

print(string,"oi")

alunos = open("alunos.txt", "r")
linha = alunos.readline()
while linha:
    linha = linha.rstrip("\n") 
    print(linha)
    linha = alunos.readline()
alunos.close()

# write(nome + "\n") pula linha
# script = string.rstrip("\n") 
# w escreve o do momento e apaga o conteúdo anterior
# a adiciona no que ja tem 