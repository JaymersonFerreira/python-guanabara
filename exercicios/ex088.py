# from random import randint
# from time import sleep
# numero = 0
# jogo = []
# qtd = int(input('Quantos números você quer que eu sorteie? '))
# for cont in range(qtd):
#     sort = 0
#     cartela = list()
#     while sort <= 6:
#         sorteio = randint(1, 60)
#         if sorteio not in cartela:
#             cartela.append(sorteio)
#             sort += 1
#     jogo.append(cartela)
# for j in range(qtd):
#     print(jogo[j])
#     sleep(0.7)

'''GUANABARA'''
'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta.'''

from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('     JOGA NA MEGA SENA       ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 30, f'SORTEANDO {quant} JOGOS ', '-= *3')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.7)
print('-=' * 4, '< BOA SORTE! >', '-=' * 4)