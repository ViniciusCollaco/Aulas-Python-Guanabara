from time import sleep
valorA = int(input('Qual o primeiro valor: '))
valorB = int(input('Qual o segundo valor: '))
print('[1]Somar \n[2]Multiplicar \n[3]Maior \n[4]Novos números \n[5]Sair do programa')
opcao = int(input('Qual é a sua opção? '))
while opcao != 5:
    if opcao == 1:
        soma = valorA + valorB
        print('A soma entre {} + {} é {}'.format(valorA, valorB, soma))
    elif opcao == 2:
        multiplicaçao = valorA * valorB
        print('A multiplicação de {} x {} é {}'.format(valorA, valorB, multiplicaçao))
    elif opcao == 3:
        if valorA > valorB:
            maior = valorA
        else:
            maior = valorB
        print('Entre {} e {} o maior é {}'.format(valorB, valorA, maior))
    elif opcao == 4:
        print('Informe os números novamente.')
        valorA = int(input('Qual o primeiro valor: '))
        valorB = int(input('Qual o segundo valor: '))
    else:
        print('Opção invalida, tente novamente')
    print('=-=' * 10)
    sleep(1)
    print('[1]Somar \n[2]Multiplicar \n[3]Maior \n[4]Novos números \n[5]Sair do programa')
    opcao = int(input('Qual é a sua opção?'))
print('Programa encerrado. Obrigado pelo uso!!!')