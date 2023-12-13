print('-=-' * 30)
print(f'Caixa La')
print('-=-' * 30)
valor = int(input('Que valor voce quer sacar ? R$ '))
total = valor 
ced = 50
totCed = 0
while True:
    if total >= ced:
        total -= ced
        totCed +=1
    else:
        if totCed > 0:
            print (f'total de {totCed} notas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totCed = 0
        if total == 0:
            break
print('-=-' * 30)
print('Volde sempre ao Caixa La.')