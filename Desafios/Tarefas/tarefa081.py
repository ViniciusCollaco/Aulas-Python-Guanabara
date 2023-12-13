lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar [S/N] ? ')).upper().strip()[0]
    if continuar == 'N':
        break
print('-=' * 30)
print(f'Voce digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O numero 5 Faz parte da lista.')
else:
    print('O numero 5 não faz parte da lista.')