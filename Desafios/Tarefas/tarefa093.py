informacoes = {}
rendimento = []
informacoes['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {informacoes["nome"]} jogou ? '))
for indice in range(0, partidas):
    rendimento.append(int(input(f'Quantos gols na partida {indice} ?')))
informacoes['gols'] = rendimento[:]
informacoes['total'] = sum(rendimento)
print('-=-'*30)
print(informacoes)
print('-=-'*30)
for indice, valor in informacoes.items():
    print(f'O campo {indice} tem o valor {valor}')
print('-=-'*30)
print(f'O jogador {informacoes["nome"]} jogou {partidas} partidas')
for indice in range(0, len(rendimento)):
    print(f'=> Na partida {indice}, fez {rendimento[indice]} gols.')
print(f'Foi um total de {sum(rendimento)} gols.')
