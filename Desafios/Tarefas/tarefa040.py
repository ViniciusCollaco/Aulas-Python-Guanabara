nota1 = float(input('Qual a primeira nota '))
nota2 = float(input('Qual a segunda nota '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print('Tirando {:.1f} e {:.1f}, aprovado com média {:.1f}'.format(nota1, nota2, media))
elif media < 5.0:
    print('Tirando {:.1f} e {:.1f}, reprovado com média {:.1f}'.format(nota1, nota2, media))
else:
    print('Tirando {:.1f} e {:.1f}, recuperação com média {:.1f}'.format(nota1, nota2, media))