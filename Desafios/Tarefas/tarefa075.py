cont = 0
numero = (int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')))
print(f'Os numeros digitados são: {numero}')
print(f'O valor 9 apareceu {numero.count(9)} vezes')
if 3 in numero:
    print(f'O valor 3 apareceu {numero.index(3)+1}° posição')
else:
    print("Não foi encontrado o número 3")
print('Os valores pares digitados foram ', end='')
for n in numero:
    if n % 2 == 0: 
        print(n, end='')


