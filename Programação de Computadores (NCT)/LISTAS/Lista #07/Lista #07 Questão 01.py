#faixa_etaria = [ [], [], [], [], [] ]
faixa_15 =    []
faixa_16_30 = []
faixa_31_45 = []
faixa_46_60 = []
faixa_60 =    []


idade = int(input('Insira sua idade: '))

i = 1

while (i <= 14):
    if idade <= 15:
        faixa_15.append(idade)
    elif 16 <= idade <= 30:
        faixa_16_30.append(idade)
    elif 31 <= idade <= 45:
        faixa_31_45.append(idade)
    elif 46 <= idade <= 60:
        faixa_46_60.append(idade)
    elif idade > 60:
        faixa_60.append(idade)
    
    i += 1

    idade = int(input('Insira sua idade: '))

print('Faixa etária até 15 anos: ', faixa_15, '\n' 'Quantidade de idades referentes à essa faixa: ', len(faixa_15), '\n' 'E a porcentagem da quantidade da faixa é: ', float(len(faixa_15)/15), '%' )
print('-'*60) 
print('Faixa etária de 16 até 30 anos: ', faixa_16_30, '\n' 'Quantidade de idades referentes à essa faixa: ', len(faixa_16_30), '\n' 'E a porcentagem da quantidade da faixa é: ', float(len(faixa_16_30)/15), '%' ) 
print('-'*60)
print('Faixa etária de 31 até 45 anos: ', faixa_31_45, '\n' 'Quantidade de idades referentes à essa faixa: ', len(faixa_31_45), '\n' 'E a porcentagem da quantidade da faixa é: ', float(len(faixa_31_45)/15), '%' ) 
print('-'*60)
print('Faixa etária de 46 até 60 anos: ', faixa_46_60, '\n' 'Quantidade de idades referentes à essa faixa: ', len(faixa_46_60), '\n' 'E a porcentagem da quantidade da faixa é: ', float(len(faixa_46_60)/15), '%' ) 
print('-'*60)
print('Faixa etária acima de 60 anos: ', faixa_60, '\n' 'Quantidade de idades referentes à essa faixa: ', len(faixa_60), '\n' 'E a porcentagem da quantidade da faixa é: ', float(len(faixa_60)/15), '%' ) 