dados = []
informacoes = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(informacoes) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    informacoes.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar [S/N] ? ')).upper().strip()[0]
    if continuar == 'N':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(informacoes)} pessoas.')
print(f'O mair peso foi de {maior}Kg. Peso de ', end='')
for pessoa in informacoes:
    if pessoa[1] == maior:
        print(f'{pessoa[0]}', end='')
print()
print(f'O menor peso foi de {menor}Kg.')
for pessoa in informacoes:
    if pessoa[1] == menor:
        print(f'{pessoa[0]}', end='')