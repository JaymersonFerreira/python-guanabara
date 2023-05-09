# import random
# from time import sleep
#
# num = random.randint(0, 10)
# chute = int(input('Vou pensar em um número de 0 a 10, tente adivinhar:  '))
# for c in range(0, 3):
#     print('.', end='')
#     sleep(0.8)
# print('', end='\n')
# cont = 0
# sleep(0.5)
# while num != chute:
#     cont += 1
#     print('\033[31mVocê errou!\033[m'.format(chute, num))
#     chute = int(input('Tente novamente, {}ª tentativa: '.format(cont+1)))
# print('\033[32mParabéns você acertou!!!\n\033[mO número pensado foi \033[34m{}\033[m!\nVocê recisou de \033[34m{}\033[m tentativas para acertar!'.format(chute, cont+1))


'''GUANABARA'''

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
palpites = 0
acertou = False
while not acertou:
    jogador = int(input('Qual é seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais..  Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou!!! com {} tentativas, Parabens!'.format(palpites))

