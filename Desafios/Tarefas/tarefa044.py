print('{:=^40}'.format(' LAJAS TABAJARA '))
valor = float(input('Preço das compras R$ '))
print('FORMAS DE PAGAMENTO\n [1] á vista dinheiro/cheque\n [2]á vista cartão\n [3]2x no cartão\n [4]3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = valor - (valor * 10 / 100)
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(valor, total))
elif opcao == 2:
    total = valor - (valor * 5 / 100)
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(valor, total))
elif opcao == 3:
    parcela = valor / 2 
    print('O total de R$ {:.2f} vai custar R$ {:.2f} em 2x sem juros'.format(valor, parcela))   
elif opcao == 4:
    vezes = int(input('Quantas parcelas ira fazer? '))
    parcela = valor * 1.20 / vezes
    total = valor * 1.20
    print('Sua compra será parcelada em {}x de R$ {:.2f} com juros.\nSua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(vezes, parcela, valor, total))
else:
    print('Opção inválida')