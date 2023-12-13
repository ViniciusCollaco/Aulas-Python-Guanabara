print('\033[0;30;41mTeste\033[m') 
print('\033[4;33;44mTeste\033[m') 
print('\033[1;35;43mTeste\033[m') 
print('\033[30;42mTeste\033[m') 
print('\033[mTeste\033[m') 
print('\033[7;30mTeste\033[m') 

#Exemplo de construção de cor nos programas
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

#Outra madeira de executar usando .format
nome = 'Vinicius'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

#outro exemplo de como executar 
nome = 'Vinicius'
cores = {'limpa':'\033[m', 
         'azul':'\033[34m', 
         'amarelo':'\033[33m', 
         'pretoebranco':'\033[7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))