contador = 0
acumulador = 1
fatorial = int(input('Qual valor voce quer fatoriar: '))
while contador < fatorial:
    contador += 1
    acumulador *= contador
print('{}! = {}'.format(fatorial, acumulador))  