from random import randint
from time import sleep

cont=0
c= randint(0,10) #faz o computador "pensar"
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
j=11
continuar='S'
while True:
    c= randint(0,10) #faz o computador "pensar"
    cont=0
    while True:
        j=int(input('Em que número eu pensei? '))
        print('Hmm...')
        sleep(1) #pausa para parecer que o computador está pensado
        if c!=j:
            print('Você errou! tente de novo', end='. ')
            if c<j:
                print('É menor que {}' .format(j))
            if c>j:
                print('É maior que {}!' .format(j))
        if j>10 or j<0:
            print('Fala sério, joga pra valer! ')
        cont+=1
        if c==j:
            break
        print('=-='*15)
    print('PARABÉNS!!!, em {} tentativas você leu meu pensamento, eu realmente estava pensando em {}'.format(cont, c))
    continuar=str(input('Foi muito divertido! Deseja jogar de novo? [S] [N]')).upper() .strip() [0]
    if continuar=='N':
        break
    while continuar!='S' and continuar!='N':
        continuar=str(input('Desculpa não entendi. Você deseja continuar? [S] [N]')).upper() .strip() [0]
print('fim')
