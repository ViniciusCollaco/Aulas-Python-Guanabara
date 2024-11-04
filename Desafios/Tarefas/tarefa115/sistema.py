from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:    
    resposta = menu(['Ver pessoas cadastrar', 'Cadastrar nova pessoas', 'Sair do sistema'])
    match resposta:
        case 1:
            # Opção de listar o conteudo de um arquivo.
            lerArquivo(arq)
        case 2:
            # Opção de cadastrar uma nova pessoa. 
            cabecalho('NOVO CADASTRO')
            nome = str(input('Nome: '))
            idade = leiaInt('Idade: ') 
            cadastrar(arq, nome, idade)
        case 3:
            # Opção de sair do sistema.
            cabecalho('Sair do sistema... Até logo!')
            break
        case _:
            # Digitou uma opção errada no menu.
            print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)