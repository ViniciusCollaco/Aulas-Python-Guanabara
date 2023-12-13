cadastro = {}
cadastro['nome'] = str(input('Nome: '))
cadastro['media'] = float(input(f'Media de {cadastro["nome"]}: '))
if cadastro['media'] >= 7:
    cadastro['situacao'] = 'aprovado'
elif 5 <= cadastro['media'] < 7:
    cadastro['situacao'] = 'recuperação'
else:
    cadastro['situacao'] = 'reprovado'
print('-=-'*30)
for chave, valor in cadastro.items():
    print(f' - {chave} é igual {valor}')