from time import sleep
def maior(* numeros):
    print('-=-'*20)
    print('Analisando os valores passados...', flush=True)
    sleep(1)
    if len(numeros) > 0:
        print(f'{numeros} foram informados {len(numeros)} valores ao todo.')
        print(f'O maior numero informado foi {max(numeros)}.')
    else:
        print('Foram informados 0 valores ao todo.')
        print('Não existe maior valor, NULL.')
        print('-=-'*20)
    
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

'''Outra maneira de realizar
def maior(* numero):
    contador = maior = 0
    print('-=-' * 30)
    print('\n Analisando os valores passados...')
    for valor in numeros:
        pront(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if contador == 0
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f'Foram informados {contador} valores ao todo.')
    print(f'Omaior valor informado foi {maior}.')
        
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()'''