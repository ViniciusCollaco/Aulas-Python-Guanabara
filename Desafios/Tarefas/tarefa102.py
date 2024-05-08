def fatorial(valor, show=False):
    fatoriValor = 1
    for contador in range(valor, 0, -1):
        if show:
            print(contador, end='')
            if contador > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fatoriValor *= contador
    return fatoriValor
print(fatorial(5))