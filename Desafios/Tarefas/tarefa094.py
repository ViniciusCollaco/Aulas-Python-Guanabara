cadastro = {}
listagem = []
acumuladorIdade = mediaIdade = 0
while True:
    cadastro['nome'] = str(input('Nome: ')).strip()
    while True:
        cadastro['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if cadastro['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    cadastro['idade'] =int(input('Idade: '))
    acumuladorIdade += cadastro['idade']
    while True:
        continuar = str(input('Deseja continuar ? [S/N] ')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    listagem.append(cadastro.copy())
    if continuar == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo  temos {len(listagem)} pessoas cadastradas')
mediaIdade = acumuladorIdade / len(listagem)
print(f'B) A média de idade é de {mediaIdade:5.2f} anos')
print('C) As mulheres cadastradas foram ', end='')
for pessoa in listagem:
    if pessoa['sexo'] == 'F':
        print(f'{pessoa["nome"]}', end=', ')
print('\nD) Lista das pessoas que estão acima da média: ')
for pessoas in listagem:
    if pessoa['idade'] >= mediaIdade:
        print('     ', end='')
        for chave, valor in pessoa.items():
            print(f'{chave} = {valor}; ', end='') 
        print()
    else:
        print('Não possui ninguem.')  
print('\n<< !!TERMINO!! >>')


