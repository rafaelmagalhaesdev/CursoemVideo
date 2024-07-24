import random
n1 = str(input('Digite o nome do aluno: '))
n2 = str(input('Digite o nome do aluno: '))
n3 = str(input('Digite o nome do aluno: '))
n4 = str(input('Digite o nome do aluno: '))
n5 = str(input('Digite o nome do aluno: '))
n6 = str(input('Digite o nome do aluno: '))
list = [n1, n2, n3, n4, n5, n6]
random.shuffle(list)
print('O aluno sorteado foi: {}'.format(list))
