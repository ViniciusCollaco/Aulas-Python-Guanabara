genero = sexo.upper()
acumulador = 0
for contagem in range(1,5):
    print('Digite a {}° pessoa'.format(contagem))
    nome = str(input('Qual é seu nome: '))
    idade = int(input('Qual é sua idade: '))
    sexo = str(input('Qual o seu sexo (M/F): '))
    media =+ idade
    if genero == F and idade <= 20:
        acumulador =+ 1
    else:
        nomeMaior = nome
        maior = idade
        nomeMenor = nome
        menor = idade
        if idade > maior:
            maior = idade
            nomeMaior = nome
        if idade < menor:
            menor = idade
            nomeMenor = nome
print('A media de idade é {}'.format(media/4))
print('O homem mais velho é {} com {} anos'.format(nomeMaior, maior))  
print('O homem mais novo é {} com {} anos'.format(nomeMenor, menor)) 
print('Existe {} mulheres com idade ate 20 anos'.format(acumulador))       
    
        
    
    
    