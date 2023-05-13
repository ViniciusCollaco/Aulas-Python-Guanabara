kg = float(input('Quantos KG voce tem: '))
altura = float(input('Qual a sua altura: '))
imc = kg / (altura ** 2)
print('O IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:  
    print('Peso normal')    
elif 25 <= imc < 30:
    print('Sobrepeso')  
elif 30 <= imc < 40:    
    print('Obesidade')
else:
    print('Obesidade Mórbida')