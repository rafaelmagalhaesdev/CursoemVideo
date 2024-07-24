from datetime import date
from time import sleep
ano = int(input('Qual ano você quer analisar? Coloque 0 para analisar o ano atual: '))
print('ANALISANDO ...')
sleep(2)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 == 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} NÃO é bissexto')