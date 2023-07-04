valor = mult = 0
print('Tabuada, caso queira sair colocar numero negativo.')
while True:
    print('-=-' * 30)
    valor = int(input('Qual valor desejado para a tabuada: '))
    print('-=-' * 30)
    if valor < 0:
        break
    for cont in range (1, 11):
        mult = cont * valor
        print(f'{valor} x {cont} = {mult}')
print('Programa encerrado, obrigado por usar!!!')