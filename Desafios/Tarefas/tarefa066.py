valor = cont = soma =0
while True:
    print('-=-' * 30)
    valor = int(input('Qual valor que voce deseja (digite 999 para parar) '))
    if valor == 999:
        print('Programa encerrado, obrigado por usar!!!')
        break
    cont += 1
    soma += valor
print('-=-' * 30)
print(f'Foram registrados {cont} e o total foi de {soma}')
    