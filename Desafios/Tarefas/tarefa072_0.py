numero = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis','Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
continuar = ' '
while True:
    resposta = int(input('Digite um número entre 0 e 20? ? '))
    if 0 <= resposta <= 20:
        print(f'Você digitou o número {numero[resposta]}')
    else:
        resposta = int(input('Digite um número entre 0 e 20? ? '))
    while continuar not in 'SN':
        continuar = str(input('Deseja contimuar [S/N]? ')).upper().strip()[0]
    if continuar == 'N':
        break
print('Obrigado por usar o programa')