from math import radians, sin, cos,tan
ang = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, seno))
coss = cos(radians(ang))
print('O ângulo de {} tem o CESSENO de {:.2f}'. format(ang, coss))
tan = tan(radians(ang))
print('O ângulo de {} tem a TANGENTE de {:.2f}'. format(ang, tan))