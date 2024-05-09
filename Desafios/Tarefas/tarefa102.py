def fatorial(valor, show=False):
    """-> Calcula o Fatorial de um número.
    :param valor: O numero a ser calculado. 
    :para show: (opicional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um valor."""
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
help(fatorial)