#Abaixo eu resolvi, porém usando muita coisa ainda, tente sempre reduzir
#km = float(input('Quantos KM foi rodado? '))
#dias = int(input('Por quantos dias foi alugado o carro? '))
#diaria = dias * 60
#kmrodado = km * 0.15
#total = diaria + kmrodado
#print('Conforme verificado, o Carro foi alugado por {}dias (R$60,00 diaria) e "rodou" {:.2f}km (RS$0,15) \nTotal a pagar: {:.2f} + {:.2f} = {:.2f}'.format(dias, km, diaria, kmrodado, total))
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))