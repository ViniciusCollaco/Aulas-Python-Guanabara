lista = []
valores = cont = 0
continuar = ''
while True:
    valores = int(input('Qual valor desejado: '))
    if valores not in lista:
        lista.append(valores)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicioná-lo.')
    continuar = str(input('Deseja continuar [S/N]? ')).upper() .strip()[0]
    if continuar == 'N':
        break
print('-=-' * 30)
lista.sort()
print(f'Você digitou os valores {lista}')