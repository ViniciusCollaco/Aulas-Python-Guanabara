somaIdade = 0
mediaIdade = 0
maiorIdade = 0
nomeMaior = ''
acumuladorMulher = 0
for contador in range (1, 5):
    print('----- Digite o nome da {}° pessoa -----'.format(contador))
    nome = str(input('Qual é seu nome: ')).strip()
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Qual é seu sexo (M/F): ')).strip()
    somaIdade =+ idade
    if contador == 1 and sexo in 'Mm':
        maiorIdade = idade
        nomeMaior = nome
    if sexo in 'Mn' and idade > maiorIdade:
        maiorIdade = idade
        nomeMaior = nome
    if sexo in 'Ff' and idade < 20:
        acumuladorMulher += 1
mediaIdade = somaIdade / 4
print('A média de idade do grupo é de {} anos'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdade, nomeMaior))
print('Ao todo são {} mulheres com menos de 20 anos'.format(acumuladorMulher))