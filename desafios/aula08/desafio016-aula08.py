#como utilizei apenas a função trunc do "math" posso usar o "from math import trunc" caso eu quissese todos
#eu poderia colocar: import math
from math import trunc
num = float(input('Digite um valor: '))
#como eu utilizei o "from math import trunc" não preciso colocar em ".format(num, math.trunc(num))) e sim apenas o
#.format(num, trunc(num)))
print('O valor digitado foi {} e sua porçao inteira é {}'.format(num, trunc(num)))
'''
Outro metodo é que nem abaixo:

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua prção inteira é {}'.format(num, int(num)))'''