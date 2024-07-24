salario = float(input('Digite o seu salário: R$ '))
if salario >=1250:
    aum = salario + (salario * 10 / 100)
else:
    aum = salario + (salario * 15 / 100)
print('Seu salario aumentou de R${}, para R${}'.format(salario, aum))