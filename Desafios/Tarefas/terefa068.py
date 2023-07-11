from random import randint
cont = 0
while True:
    jogador = int(input('Qual numero voce quer ? '))
    computador = randint(0,11)
    total = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('PAR ou IMPAR ? ')).strip() .upper() [0]
    print(f'Voce jogou {jogador} e o computador jogou {computador}. O total deu {total} ')
    print('é PAR' if total % 2 == 0 else 'é IMPAR')
    if escolha == 'P':
        if total % 2 == 0:
            print('Voce VENCEU!!')
            cont += 1
        else:
            print('Voce PERDEU')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('Voce VENCEU!!')
            cont += 1
        else:
            print('Voce PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER ! Voce venceu {cont} vezes')