distancia = float(input('Qual a distância da sua viagem? '))
if distancia <=200:
    val1 = (distancia * 0.50)
    print(f'O valor que irá pagar é de R${val1}')
else:
    val2 = (distancia * 0.45)
    print(f'Como você está em uma viagem de maior que {distancia}Km, você pagará R$0,45 por Km, sendo assim será um total de {val2} ')
print(f'Você está preste a começar um viagem com {distancia}Km')