import moeda 
valor = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.formatacao(valor)} é {moeda.metade(valor, True)}')
print(f'O dobro de {moeda.formatacao(valor)} é {moeda.dobro(valor, True)}')
print(f'Aumento 10%, temos {moeda.aumentar(valor, 10, True)}')
print(f'Diminuir 13%, temos {moeda.diminuir(valor, 13, True)}')