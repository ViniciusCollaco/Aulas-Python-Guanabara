print('Gerador de PA')
print('-=' * 10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
conta = 1
pergunta = 10
total = 0
while pergunta != 0:
    total += pergunta
    while conta <= total:
        print('{}'.format(termo), end=" - ")
        conta += 1
        termo += razao
    print('ACABOU')
    pergunta = int(input('Quantos termos voce gostaria: '))
print('Progressão finalizada com {} termos mostrados'.format(total))