def voto(anoNac):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - anoNac
    if idade < 16:
        return print(f'Com {idade} anos: VOTO NEGADO.')
    elif idade > 65 or 16 <= idade < 18:
        return print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
# Programa principal
anoNac = int(input('Em que ano você nasceu ? '))
voto(anoNac)
