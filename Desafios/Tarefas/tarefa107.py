import moeda
valor = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {valor} é R$ {moeda.metade(valor)}')
print(f'O dobro de R$ {valor} è R$ {moeda.dobro(valor)}')
print(f'Aumento 10%, temos R$ {moeda.aumentar(valor)}')
print(f'Diminuir 13%, temos R$ {moeda.diminuir(valor)}')