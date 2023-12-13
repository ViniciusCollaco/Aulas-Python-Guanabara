contIdade = contMasc = contFemin = 0
cont = 1
while True:
    print('-=-' * 30)
    print(f'Cadastro da {cont}° pessoa')
    print('-=-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip() .upper()[0]
    if idade > 18:
        contIdade += 1
    if sexo == 'M':
        contMasc += 1
    if sexo == 'F' and idade < 20:
        contFemin += 1
    cont += 1
    print('-=-' * 30)
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input('Deseja continuar ? [S/N]')).strip() .upper()[0]
    if continuar == 'N':
        break
print('-=-' * 30)
print(f'Total de pessoas com mais de 18 anos: {contIdade}')
print(f'Ao todo temos {contMasc} homens cadastrados')
print(f'Temos {contFemin} mulheres com menos de 20 anos.')
    
        