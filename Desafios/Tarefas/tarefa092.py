from datetime import datetime
carteiraTrabalho = {}
carteiraTrabalho['nome'] = str(input('Nome: '))
anoNasc = int(input('Ano de nascimento: '))
carteiraTrabalho['idade'] = datetime.now().year - anoNasc
carteiraTrabalho['ctps'] = int(input('Carteira dde trabalho (valor 0 caso não tenha): '))
if carteiraTrabalho['ctps'] != 0:
    carteiraTrabalho['contratacao'] = int(input('Ano de contratação: '))
    carteiraTrabalho['salario'] = float(input('Salario R$ '))
    carteiraTrabalho['aposentadoria'] = carteiraTrabalho['idade'] + ((carteiraTrabalho['contratacao'] + 35) - datetime.now().year)
    print('-=-'*30)
for chave, valor in carteiraTrabalho.items():
    print(f'- {chave} tem o valor {valor}')