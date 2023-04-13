pre = float(input('Qual o preço do produto ? R$ '))
desc = pre - (pre * 5 / 100) 
print('O produto com o valor de R$ {:.2f}, com 5% fica no valor de R$ {:.2f}'.format(pre, desc))