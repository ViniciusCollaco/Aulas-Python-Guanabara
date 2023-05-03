casa = float(input('Qual o valor da casa? '))
salario = float(input('Quanto é seu salario? '))
anos = int(input('Quantos anos pretende pagar? '))
prestacao = casa / (anos * 12)
porcentagem = salario * 0.3
print('Para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}'.format(casa, anos, prestacao))
if porcentagem <= prestacao:
   print('Emprestimo \033[1;31;41mNEGADO\033[m') 
else:
    print('Emprestimo \033[1;32;42mAPROVADO\033[m')

