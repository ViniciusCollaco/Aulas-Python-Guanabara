from math import radians, sin, cos, tan
ang = int(input('Digite o valor do angulo: '))
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print('O valor de seno é {:.2f} \nO valor de cosseno é {:.2f} \nO valor de tangente é {:.2f}'.format (seno, coss, tang))