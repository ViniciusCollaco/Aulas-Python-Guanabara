def leiaInt(valor):
    while True:
        try:
            inteiro = int(input(valor))
        except (ValueError, TypeError):
            print("\033[31mERRO! Digite um número inteiro.\033[m")
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferio não digitar esse número.\033[m')
            return 0
        else:
            return int(inteiro)
            
def leiaReal(valor):
    while True:
        try:
            real = float(input(valor))
        except (ValueError, TypeError):
            print("\033[31mERRO! Digite um número real.\033[m")
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferio não digitar esse número.\033[m')
            return 0
        else:
            return float(real)
inteiro = leiaInt('Digite um número inteiro: ')
real = leiaReal('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
