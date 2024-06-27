import moeda 
valor = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.formatacao(valor)} é {moeda.formatacao(moeda.metade(valor))}')
print(f'O dobro de {moeda.formatacao(valor)} é {moeda.formatacao(moeda.dobro(valor))}')
print(f'Aumento 10%, temos {moeda.formatacao(moeda.aumentar(valor, 10))}')
print(f'Diminuir 13%, temos {moeda.formatacao(moeda.diminuir(valor, 13))}')