def linha (tamanho=42):
    print("-" * tamanho)
    
def leiaInt(valor):
    while True:
        try: 
            numero = input(valor)
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mUsuário preferiu não digitar esse número.\033[m")
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
        print(f'{contador} - {item}')
        contador += 1
    linha()
    opcao = leiaInt('Sua Opção: ')
    return opcao