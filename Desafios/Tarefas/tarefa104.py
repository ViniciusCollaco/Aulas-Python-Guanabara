def leiaInt(valor):
    while True:
        numero = input(valor)
        if numero.isnumeric():
            return int(numero)
            break
        else:
            print("\033[31mERRO! Digite um número inteiro.\033[m")
numero = leiaInt('Digite um número: ')
print(f'Voce acabou de digitar o número {numero}')