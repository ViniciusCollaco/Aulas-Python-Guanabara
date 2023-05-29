acumulador = 0
cont = 0
for laco in range(1, 7):
    valor = int(input('Qual o {}° valor: '.format(laco)))
    if valor % 2 == 0:
        cont = cont + 1
        acumulador += valor
print('A soma dos {} numeros pares é {}'.format(cont, acumulador))