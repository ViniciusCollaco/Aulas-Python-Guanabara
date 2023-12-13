from random import randint 
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
maquina = randint(0, 2)
print('Sua opção: \n[0] PEDRA \n[1]PAPEL \n[2]TESOURA')
usuario = int(input('Qual é a sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[maquina]))
print('Jogador jogou {}'.format(itens[usuario]))
print('-=' * 11)
if usuario == 0 and maquina == 2:
    print('Você ganhou!')
elif usuario == 1 and maquina == 0:
    print('Você ganhou!')
elif usuario == 2 and maquina == 1:
    print('Você ganhou!')
elif usuario == 0 and maquina == 0:
    print('Você empatou!')
elif usuario == 1 and maquina == 1:
    print('Você empatou!')
elif usuario == 2 and maquina == 2:
    print('Você empatou!')
elif usuario == 0 and maquina == 1:
    print('Você perdeu!')
elif usuario == 1 and maquina == 2:
    print('Você perdeu!')
elif usuario == 2 and maquina == 0:
    print('Você perdeu!')
else:   
    print('Opção inválida! Tente novamente')


