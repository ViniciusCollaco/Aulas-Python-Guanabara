pergunta = 'S'
media = 0
cont = maior = menor = acumulador = 0
while pergunta in 'Ss':
    valor = int(input('Qual numero voce quer: '))
    acumulador += valor
    cont += 1
    if cont == 1:
        maior = menor = valor
    else: 
        if valor > maior :
            maior = valor
        if valor < menor:
            menor = valor
    pergunta = str(input('Deseja continuar [S/N]')).strip().upper()[0]
media = acumulador / cont
print('A media dos valores foi de {:.2f}, foi no total de {} numeros, o maior numero é {}, e o menor numero é {}'.format(media, cont, maior, menor))

'''print(f'A media dos valores foi de {media:.2f}, foi no total de {cont} numeros, o maior numero é {maior}, e o menor numero é {menor}')'''    