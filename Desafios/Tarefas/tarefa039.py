from datetime import date
sexo = str(input('Digite M para masculino ou F para feminino: '))
genero = sexo.upper()
if genero == 'F':
    print('Voce não precisa se alistar.')
elif genero == 'M':
    atual = date.today().year
    nascimento = int(input('Em qual ano voce nasceu: '))
    idade =  atual - nascimento
    tempoFaltante = 18 - idade 
    anoIngreso = atual + tempoFaltante
    print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade , atual))
    if idade < 18:
        print('Ainda falta {} anos para o alistamento. \nSeu alistamento sera em {}.'.format(tempoFaltante, anoIngreso))
    elif idade > 18:
        print('Você já deveria ter se alistado há {} anos. \nSeu alistamento foi em {}.'.format(tempoFaltante*-1, anoIngreso))
    else:
        print('Você tem que se alistar imediatamente')
else:
    print('Opção invalida, tente novamente')
    