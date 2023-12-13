total = contPro = cont = precoBarat = 0
prodBart = ' '
print('-=-' * 30)
print('LOJA QUEIMA')
print('-=-' * 30)
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    total += preco
    cont += 1
    if preco > 1000:
        contPro += 1
    if cont == 1 or preco < precoBarat:
        precoBarat = preco
        prodBart = produto
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Deseja continuar ? [S/N]')).strip() .upper() [0]
    if pergunta == 'N':
        break
print(f'O total foi de R$ {total:.2f}')
print(f'Foi no total de {contPro} produtos que custa mais de R$ 1000.00')
print(f'O produto mais barato é {prodBart} que custa R$ {precoBarat:.2f}')