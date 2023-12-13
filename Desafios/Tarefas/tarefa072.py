numero = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis','Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
continua = ' '
while True:
    resposta = int(input('Digite um número entre 0 e 20? ? '))
    if 0 <= resposta <= 20:
        break
    print('Tente novamente. ', end=' ')
print(f'Você digitou o número {numero[resposta]}')
    
