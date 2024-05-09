def ficha(valorNome='<desconhecido>', numeroGols=0):
    print(f'O jogador {valorNome} fez {numeroGols} gol(s) no campeonato.')
nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(numeroGols=gols)
else:
    ficha(nome, gols)