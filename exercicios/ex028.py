# import random
#
# num = random.randint(0, 5)
# chute = int(input('Qual o número que foi gerado: '))
# if num == chute:
#     print('Você acertou! Você digitou: {}, e o número gerado foi: {}'.format(chute, num))
# else:
#     print('Você errou! Você digitou: {}, e o número gerado foi: {}'.format(chute, num))

from random import randint
from time import sleep

computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número tente adivinhar...')
print('-=-'* 20)
jogador = int(input('Em que único eu pensei? ')) # jogador tenta adivinhar
print('PRCESSANDO...')
sleep(1)
if jogador == computador:
    print('PARABENS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))