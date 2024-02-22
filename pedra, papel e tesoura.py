# pedra, papel e tesoura

from random import randint
from time import sleep

itens = ('Pedra' , 'Papel' , 'Tesoura')
b= randint (0, 2)                            #COMPUTADOR
j= int(input('''Escolha:
\033[35mPEDRA   [0] \033[m
\033[36mPAPEL   [1] \033[m
\033[33mTESOURA [2] \033[m'''))              #JOGADOR
if j != 0 and j != 1 and j != 2:
    print('\033[30;41mJogada inválida\033[m')
else:
    print('\033[32;45mJO\033[m')
    sleep(1)
    print('\033[35;42mKEN\033[m')
    sleep(1)
    print('\033[32;45mPO!!!\033[m')
    sleep(1)
    print('\033[30m-=\033[m' * 14)
    print('O \033[35mcomputador\033[m jogou \033[7;35m{}\033[m' .format(itens[b]))
    print('O \033[36mjogador\033[m jogou \033[7;36m{}\033[m'.format(itens[j]))
    print('\033[30m-=\033[m' * 14)

    if j == 0 and b == 0:
        print('\033[35mDEU EMPATE\033[m')
    elif j == 0 and b == 1:
        print('\033[31mVOCÊ PERDEU\033[m')
    elif j == 0 and b == 2:                      #PEDRA
        print('\033[32mVOCÊ GANHOU\033[m')
    elif j == 1 and b == 1:
        print('\033[35mDEU EMPATE\033[m')
    elif j == 1 and b == 2:
        print('\033[31mVOCÊ PERDEU\033[m')
    elif j == 1 and b == 0:                      #PAPEL
        print('\033[32mVOCÊ GANHOU\033[m')
    elif j == 2 and b == 2:
        print('\033[35mDEU EMPATE\033[m')
    elif j == 2 and b == 0:
        print('\033[31mVOCÊ PERDEU\033[m')
    elif j == 2 and b == 1:                      #TESOURA
        print('\033[32mVOCÊ GANHOU\033[m')
