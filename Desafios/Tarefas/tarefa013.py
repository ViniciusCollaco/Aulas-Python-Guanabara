sal = float(input('Qual o seu salario ? R$ '))
aum = sal + (sal * 15 / 100)
print('Seu salario era R$ {:.2f}, agora com 15% sera de R$ {:.2f}'.format(sal, aum))