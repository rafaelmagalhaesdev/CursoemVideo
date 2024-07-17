# Como eu fiz está em comentario: n1 = float(input('Qual é o preço do produto? R$ '))
# Como eu fiz está em comentario: desc = n1 - (n1 * 0.05)
# Como eu fiz está em comentario: print('O valor do produto com desconto de 5% é de:{:.2f}R$'.format(desc))
# Como fazer mais "leve e sintaxe melhor"
preco = float(input('Qual é o preço do produto? R$ '))
novo = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, novo))