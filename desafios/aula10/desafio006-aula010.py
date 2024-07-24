a = int(input('Primeiro número: '))
b: int = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
#Verificando qual é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando qual é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O MENOR valor é: {}, e o MAIOR valor foi: {}".format(menor, maior))
