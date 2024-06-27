def leiDinheiro(mensagem):
    validador = False
    while not validador:
        entrada = str(input(mensagem)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mErro: \"{entrada}\" é um preço inválido!\033[m')
        else:
            validador = True
            return float(entrada)