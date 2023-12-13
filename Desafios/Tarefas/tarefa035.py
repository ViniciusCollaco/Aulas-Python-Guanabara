print('-='*20)
print('Analisador de triângulos')
print('-='*20)
a = float(input('Qual o primeiro valor: '))
b = float(input('Qual o segundo valor: '))
c = float(input('Qual o terceiro valor: '))
if a + b > c and a + c > b and b + c > a :
    print('Os segmantos acima PODEM FORMAR triangulo')
else:
     print('Os segmantos acima NÃO PODEM FORMAR triangulo')