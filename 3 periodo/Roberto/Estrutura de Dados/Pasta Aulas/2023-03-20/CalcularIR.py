arq = open("funcionarios.txt","r")
arq_saida = open("folha_pagamento.txt","w")

arq_saida.write = ("Folha de pagamento - Março de 2023 \n")
arq_saida.write = ("=" * 30)

for linha in arq:

    salario_bruto = float(salario_bruto)
    nome,salario_bruto = linha.rstrip("\n").split(",")

    if salario_bruto < 1302.00:
        inss = salario_bruto * 0.075
    elif salario_bruto < 2571.29:
        inss = (salario_bruto * 0.09) 
    elif salario_bruto < 3856.94:
        inss = (salario_bruto * 0.12) 
    elif salario_bruto < 7507.49:
        inss = (salario_bruto * 0.14) 
    else:
        inss = (7507.49 * 0.14) 

    duducao_dependente = qtd_dependente * 189.59
    # irrf = (salario_bruto-inss-duducao_dependente)
    if irrf < 1903.98:
        irrf = 0.0
    elif irrf

