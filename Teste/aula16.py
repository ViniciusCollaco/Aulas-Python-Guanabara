lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for comida in lanche:
    print(f'Eu vou comer {comida}') #Informando normalmente a tupla

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')#Para uso de informar a posição   

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}') #Para uso de informar a posição   

print('Comi pra caramba!')

print(sorted(lanche)) #Deixa em ordem quando for mostrar em tela, ele nãoo altera a tupla

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #Unifica as duas tuplas
print(c.index(2, 1)) #Em que local esta apartir de um valor

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa) #Exclui na memoria.
print(pessoa)