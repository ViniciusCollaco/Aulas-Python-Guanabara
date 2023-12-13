cont = valor = resultado = 0
while valor != 999:
    valor = int(input('Digite um valor [aperte 999 para parar]: '))
    if valor != 999:
        resultado += valor
        cont += 1
print('Vode digitou {} e a soma entre eles foi {}'.format(cont, resultado))
    