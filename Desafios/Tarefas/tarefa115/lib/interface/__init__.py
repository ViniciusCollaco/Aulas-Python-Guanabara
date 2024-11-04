def linha (tamanho=42):
    print("-" * tamanho)
    
def leiaInt(valor):
    while True:
        try: 
            numero = int(input(valor))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31m\nUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return numero
    
def cabecalho(texto):
    linha()
    print(texto.center(42))
    linha()
    
def menu(lista):
    cabecalho('MENU PRINCIPAL')
    contador = 1
    for item in lista:
        print(f'\033[33m{contador}\033[m - \033[34m{item}\033[m')
        contador += 1
    linha()
    opcao = leiaInt('\033[32mSua Opção: \033[m')
    return opcao
