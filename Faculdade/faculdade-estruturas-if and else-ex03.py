nota1 = float(input('Digite a nota: '))
media = nota1
if (media>=7.0):
    situacao = 'Aprovado'
elif (media>=5.0):
    situacao = 'Em recuperação'
else:
    situacao = 'Reprovado'
print(f'O estudante está {situacao}')