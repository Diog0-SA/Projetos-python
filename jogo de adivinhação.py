from random import randint
from time import sleep

cont=0
c= randint(0,10) #faz o computador "pensar"
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
j=11
while c!=j:
    while c!=j:
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
        print('=-='*15)
print('PARABÉNS!!!, em {} tentativas você leu meu pensamento, eu realmente estava pensando em {}'.format(cont, c))
print('fim')
