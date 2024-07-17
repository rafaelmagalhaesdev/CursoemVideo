lista = [10, 2, 5, 7, 6,3]
n = len(lista) #len é igual a elementos
soma=0
for i in range(n): #for: é "percorrer" dentro de um "range" um intervalo
    if(lista[i]%2==0):
        soma=soma+lista[i]
print(f'O somatório dos elementos pares da lista é: {soma}')