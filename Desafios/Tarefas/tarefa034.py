salario = float(input('Qual é o salario do funcionario ? R$ '))
if salario <= 1250.00:
    pagamento = salario * 1.15
else:
    pagamento = salario * 1.10
print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora.'.format(salario, pagamento))
    