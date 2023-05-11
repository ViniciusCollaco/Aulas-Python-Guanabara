valor = int(input('Digite um número inteiro: '))
print('Escolha uma das opções:\n [ 1 ] converter para BINÁRIO\n [ 2 ] converter para OCTAL\n [ 3 ] converter para HEXADECIMAL\n')
escolha = int(input('Qual a opção: '))
if escolha == 1:
    print('{} convertido para BINARIO é igual a {}'.format(valor, bin(valor)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}'.format(valor, oct(valor)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(valor, hex(valor)[2:]))
else:
    print('Opção invalida, digite novamente !')

