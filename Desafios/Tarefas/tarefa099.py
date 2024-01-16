from time import sleep
def maior(* numeros):
    print('-=-'*20)
    print('Analisando os valores passados...')
    sleep(0.5)
    if len(numeros) > 0:
        print(f'{numeros} foram informados {len(numeros)} valores ao todo.')
        print(f'O maior numero informado foi {max(numeros)}.')
    else:
        print('Foram informados 0 valores ao todo.')
        print('Não existe maior valor, NULL.')
    
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
