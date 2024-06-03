from time import sleep
pigmento = ('\033[m', 
            '\033[0;30;41m', 
            '\033[0;30;42m', 
            '\033[0;30;43m', 
            '\033[0;30;44m', 
            '\033[0;30;45m', 
            '\033[7;30m')

def ajuda(comando):
    titulo(f'Acessando o manula do comando \'{comando}\'', 4)
    print(pigmento[6], end='')
    help(comando)
    print(pigmento[0], end='')
    sleep(2)
    
def titulo(mensagem, cor=0):
    tamanho = len(mensagem) + 4
    print(pigmento[cor], end='')
    print('~'*tamanho)
    print(f'  {mensagem}')
    print('~'*tamanho)
    print(pigmento[0], end='')
    sleep(1)
    
comando = ''
while True:
    titulo('Sistema de ajuda PyHELP', 2)
    comando = str(input('Função ou Biblioteca (FIM para sair)> '))
    if comando.upper().strip() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO!', 1)