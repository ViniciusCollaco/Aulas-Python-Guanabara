teste = list()
teste.append('Gustavo')
teste.append(40)
grupo = list()
grupo.append(teste[:])
teste[0] = 'Maria'
teste [1] = 22
grupo.append(teste[:])
print(grupo)

povao = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(povao[0])
print(povao[0][0])
print(povao[2][1])
for p in povao:
    print(f'{p[0]} tem {p[1]} anos de idade.')
    
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    print('-=-' * 30)
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')