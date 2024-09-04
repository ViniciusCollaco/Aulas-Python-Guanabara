def leiaInt(valor):
    while True:
        try: 
            numero = int(input(valor))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return numero

def leiaFloat(valor):
    while True:
        try: 
            numero = int(input(valor))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return numero