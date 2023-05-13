print('Analisador de triângulos')
a = float(input('Qual o primeiro segmento: '))
b = float(input('Qual o segundo segmento: '))
c = float(input('Qual o terceiro segmento: '))
if a + b > c and a + c > b and b + c > a :
    if a == b == c == a:
        print('Os segmentos acima PODEM formar um triângulo EQUILÁTERO.')
    elif a != b != c != a:
        print('Os segmentos acima PODEM formar um triângulo ESCALENO.')
    else:
        print('Os segmentos acima PODEM formar um triângulo ISÓSCELES.')
else:
     print('Os segmantos acima NÃO PODEM FORMAR triangulo')