jogadores = []
informacoes = {}
rendimento = []
while True:
    informacoes.clear()
    informacoes['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {informacoes["nome"]} jogou ? '))
    rendimento.clear()
    for indice in range(0, partidas):
        rendimento.append(int(input(f'Quantos gols na partida {indice+1} ? ')))
    informacoes['gols'] = rendimento[:]
    informacoes['total'] = sum(rendimento)
    jogadores.append(informacoes.copy())
    while True:
        continuar = str(input('Deseja continuar ? [S/N] ')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if continuar == 'N':
        break
print('-=-'*30)
print('cod', end='')
for indice in informacoes.keys():
    print(f'{indice:<15}', end='')
print()
print('-'*40)
for chave, valor in enumerate(jogadores):
    print(f'{chave:>3} ', end='')
    for dado in valor.values():
        print(f'{str(dado):<15}', end='')
    print()
print('-'*40)
while True:
    pesquisa = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if pesquisa == 999:
        break
    if pesquisa >= len(jogadores):
        print(f'Erro! Código {pesquisa} não existe. Tente novamente.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[pesquisa]["nome"]}:')
        for indice, gol in enumerate(jogadores[pesquisa]["gols"]):
            print(f'     Na partida {indice+1}, fez {gol} gols.')
    print('-'*40)
print('<< OBRIGADO POR UTILIZAR, VOLTE SEMPRE >>')