arq = open("funcionarios.txt","r")
save = open("folha_pagamento.txt","w")
irrf = 0
save.write("Folha de Pagamento - Marco de 2023 "+ ("\n") + "="*40 + ("\n"))
for linha in arq:
    lista = linha.rstrip("\n").split(",")

    if float(lista[1]) < 1903.96:
        if float(lista[1]) < 1302.01:
            inss = float(lista[1]) * 0.075
            irrf = 0
            imposto = inss + irrf
            salario = float(lista[1]) - imposto
            str1 = str(lista[0]) + ("\n") + "salario: ," + str(lista[1]) +" INSS: ,"+ str(inss) + " IRRF: ," + str(irrf) +" imposto: ," + str(imposto) +" Salario liquido: " + str(salario) + ("\n")+ "=" *40 + ("\n")
            print(str1)
            save.write(str1)
        elif float(lista[1]) < 2571.29 and float(lista[1]) < 1903.96:
            inss = float(lista[1]) * 0.09
            irrf = 0
            imposto = inss + irrf
            salario = float(lista[1]) - imposto
            str1 = str(lista[0]) + ("\n") + "salario: " + str(lista[1]) +" INSS: "+ str(inss) + " IRRF: " + str(irrf) +" imposto: " + str(imposto) +" Salario liquido: " + str(salario) + ("\n")+ "=" *40 + ("\n")
            print(str1)
            save.write(str1)

    else:
        if float(lista[1]) > 1903.98:
            if float(lista[1]) < 2826.65:
                inss = float(lista[1]) * 0.09
                irrf = (float(lista[1]) - inss - (189.59 * int(lista[2]))) * 0.075 - 142
                imposto = inss + irrf
                salario = float(lista[1]) - imposto
                str1 = str(lista[0])+ ("\n") +"salario: " + str(lista[1]) +" INSS: "+ str(inss) + " IRRF: " + str(irrf) +" imposto: " + str(imposto) +" Salario liquido: " + str(salario) + ("\n")+ "=" *40 + ("\n")
                print(str1)
                save.write(str1)
            
            else:
                if float(lista[1]) < 3751.05 :
                    inss = float(lista[1]) * 0.12
                    irrf = (float(lista[1]) - inss - (189.59 * int(lista[2]))) * 0.15 - 354.80
                    imposto = inss + irrf
                    salario = float(lista[1]) - imposto
                    str1 = str(lista[0])+ ("\n") +"salario: " + str(lista[1]) +" INSS: "+ str(inss) + " IRRF: " + str(irrf) +" imposto: " + str(imposto) +" Salario liquido: "+ str(salario) + ("\n")+ "=" *40 + ("\n")
                    print(str1)
                    save.write(str1)
                    
                else:
                    if float(lista[1]) < 4664.68 :
                        inss = float(lista[1]) * 0.12
                        irrf = (float(lista[1]) - inss - (189.59 * int(lista[2]))) * 0.225 - 636.13
                        imposto = inss + irrf
                        salario = float(lista[1]) - imposto
                        str1 = str(lista[0])+ ("\n") +"salario: " + str(lista[1]) +" INSS: "+ str(inss) + " IRRF: " + str(irrf) +" imposto: " + str(imposto) +" Salario liquido: "+ str(salario) + ("\n")+ "=" *40 + ("\n")
                        print(str1)
                        save.write(str1)
                        
                    else:
                        if float(lista[1]) > 4664.68 :
                            inss = float(lista[1]) *0.14
                            irrf = (float(lista[1]) - inss - (189.59 * int(lista[2]))) * 0.275 - 869.36
                            imposto = inss + irrf
                            salario = float(lista[1]) - imposto
                            str1 = str(lista[0])+ ("\n") +"salario: " + str(lista[1]) +" INSS: "+ str(inss) + " IRRF: " + str(irrf) +" imposto: " + str(imposto) +" Salario liquido: "+ str(salario) + ("\n")+ "=" *40 + ("\n")
                            print(str1)
                            save.write(str1)
arq.close()
save.close()                   