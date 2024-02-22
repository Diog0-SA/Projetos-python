#Dado de 6 lados

from time import sleep
from random import choice

dado=[1, 2, 3, 4, 5, 6]
re=choice(dado)
print('Chacoalhando o dado')
sleep(0.5)
print('E o resultado é...')
sleep(1)
print('{}!' .format(re))
