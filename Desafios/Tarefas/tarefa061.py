print('Gerador de PA')
print('-=' * 10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
conta = 0
while conta < 10:
    print('{}'.format(termo), end=" - ")
    conta += 1
    termo += razao
print('ACABOU')

