a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
maior = a
if b > a and b > c:
    maior = b
if c > b and c > a: 
    maior = c
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O maior numero digitado foi {}'.format(maior))
print('O menor numero digitado foi {}'.format(menor))
