salario = float(input('Qual é o salario do Funcionário? R$'))
aum = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, recebeu um aumento de 15%, e com isso passa a receber R${:.2f}'.format(salario, aum))