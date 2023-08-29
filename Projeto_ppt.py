import os
import random

class Jogo:
    def __init__(self) -> None:
        self.voce = 0
        self.computador = 0
        
game = Jogo()
mensagem =''
while True:
    os.system('cls')
    print('==============================================================')
    print('{:^}'.format('Bem vindo ao jogo de Pedra, Papel ou Tesoura.'))
    print('==============================================================')
    print(mensagem)
    comp = str(random.randint(0,2))
    resultados = {'0':('Pedra','2'),'1':('Papel','0'),'2':('Tesoura','1')}
    print(f'PLACAR:')
    print(f'Você: {game.voce}')
    print(f'Computador: {game.computador}')
    print('==============================================================')
    print('Escolha seu lance:')
    seu_lance = input('0 - Pedra | 1 - Papel | 2 - Tesoura | ou 9 para sair\n')
    
    if seu_lance not in list('0129'):
        mensagem = 'Valor inválido'
    
    elif seu_lance == '9':
        break
    elif seu_lance == comp:
        mensagem = f'{resultados[seu_lance][0]} contra {resultados[comp][0]}. Empate'

    elif comp == resultados[seu_lance][1]:
        mensagem = f'{resultados[seu_lance][0]} contra {resultados[comp][0]}. Você ganhou'
        game.voce += 1
    else:
        mensagem = f'{resultados[seu_lance][0]} contra {resultados[comp][0]}. Você perdeu'
        game.computador += 1
