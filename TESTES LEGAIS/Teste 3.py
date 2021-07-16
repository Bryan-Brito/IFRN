#!/usr/bin/python
 
# impostos.py
# Calcula o valor do INSS e Imposto de Renda descontados em folha do funcionario
 
def readFloat(s, d):
  v = input (s)
  if not v: 
    return d
  return float(v)
 
FAIXAS = [ 4664.68, 3751.05, 2826.65, 1903.98 ]
ALIQUOTAS = [ 27.5, 22.5, 15.0, 7.5 ]
 
nome = input( "Nome: " )
salarioBruto = readFloat("Salario Bruto(1000): ",1000)
inss = readFloat("Aliquota INSS ( % ): ", 11)
 
valorInss = salarioBruto * (inss/100)
 
saldoIR = salarioBruto - valorInss
valorIR = 0
for a,b in zip(FAIXAS, ALIQUOTAS):
  if saldoIR > a: 
    valorIR += ( saldoIR - a ) * ( b/100 )
    saldoIR -= ( saldoIR - a ); 
 
salarioLiquido = salarioBruto - valorInss - valorIR
 
print ("Nome: ", nome)
print ("Salario Bruto:", salarioBruto)
print ("INSS:", valorInss)
print ("IR:", valorIR)
print ("Liquido:", salarioLiquido)