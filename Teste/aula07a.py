#n1 = int(input('Um valor: '))
#n2 = int(input('Outro valor: '))
#print('A soma vale {}'.format(n1+n2)) 

n1 = int(input('Um valor: '))
n2 = int(input('Outro Valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {}, e a \n divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))