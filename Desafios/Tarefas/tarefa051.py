termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
result = termo + (10 - 1) * razao
for cont in range(termo,result + 1, razao):
    print('{}'.format(cont), end=" - ")
print('ACABOU')