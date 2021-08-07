idade = 0
total_faixa_1 = 0
porcentagem_1 = 0
total_faixa_2 = 0
porcentagem_2 = 0
total_faixa_3 = 0
porcentagem_3 = 0
total_faixa_4 = 0
porcentagem_4 = 0
total_faixa_5 = 0
porcentagem_5 = 0

for i in range(1,16):
    print("{}ªidade".format(i))
    idade = int (input("Informe a idade:"))
    if idade <= 15:
        total_faixa_1 = total_faixa_1 + idade
        porcentagem_1 = ((total_faixa_1/100)*15)
    if idade > 15 and idade <= 30:
        total_faixa_2 = total_faixa_2 + idade
        porcentagem_2 = ((total_faixa_2/100)*15)
    if  idade > 30  and idade <= 45:
        total_faixa_3 = total_faixa_3 + idade
        porcentagem_3 = ((total_faixa_3/100)*15)
    if idade > 45 and idade <= 60:
        total_faixa_4 = total_faixa_4 + idade
        porcentagem_4 = ((total_faixa_4/100)*15)
    if idade > 60:
        total_faixa_5 = total_faixa_5 + idade 
        porcentagem_5 = ((total_faixa_5/100)*15)
              
print("Faixa etária até 15 anos \n" + "somatória da 1º faixa:",total_faixa_1)
print("porcentagem da 1º faixa:", porcentagem_1)
print("____")
print("Faixa etária de 16 a 30 anos: \n " + "somatória da 2ª faixa", total_faixa_2)
print("Porcentagem da 2ª faixa:", porcentagem_2)
print("___")
print("Faixa etária de 31 a 45 anos: \n" + "somatória da 3ª faixa", total_faixa_3)
print("Porcentagem da 3ª faixa: \n", porcentagem_3)
print("____")
print("Faixa etária de 46 a 60 anos: \n" + "somatória da 4ª faixa", total_faixa_4)
print("porcentagem da 4ª faixa:", porcentagem_4)
print("___")
print("Faixa etária acima dos 60 anos: \n" + "somatória da 5ª faixa", total_faixa_5)
print("Porcentagem da 5ª faixa:", porcentagem_5)

lista_geral = [ ['Até 15 anos' ,total_faixa_1, porcentagem_1],  
              ['De 16 a 30 anos',total_faixa_2, porcentagem_2],
              ['De 31 a 45 anos ', total_faixa_3, porcentagem_3],
              ['De 46 a 60 anos', total_faixa_4, porcentagem_4],
              ['Acima de 60 anos', total_faixa_5, porcentagem_5] ]
print( '\n', lista_geral[0], '\n',  lista_geral[1], '\n', lista_geral[2], '\n', lista_geral[3], '\n', lista_geral[4])