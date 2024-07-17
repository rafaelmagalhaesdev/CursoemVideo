n1 = float(input('Quantos reais você tem? R$: '))
dolar = n1 / 5.42
euro = n1 / 5.87
iene = n1 /0.34
print('Considerando que você tem hoje: {}R$ segue a tabela de conversão abaixo: \nDOLAR: {:.2f} US$ \nEURO: {:.2f} € \nIENE: {:.2f} ¥'.format(n1, dolar, euro, iene))