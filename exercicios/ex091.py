'''GUANABARA'''
'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, 
sabendo que o vencedor tirou o maior número no dado.'''
# from random import randint
# from time import sleep
# from operator import itemgetter
# #Dividido em 4 partes
# #1ª_Sorteia os números e depois e atribui a cada jogador dentro do dicionário
# jogo = {'jogador1': randint(1, 6),
#         'jogador2': randint(1, 6),
#         'jogador3': randint(1, 6),
#         'jogador4': randint(1, 6)}
# #
# #2_Mostra os jogadores sorteados com os números
# ranking = list()
# print('Valores sorteados:')
# for k, v in jogo.items():   #Para cada Chave e Valores em jogo
#     print(f'{k} tirou o {v} no dado.')
#     sleep(0.7)
# #3ª_Ordena usando a parte 1, que é em ordem de VALOR do dicionario, no caso os números sorteados, e em ordem reversa
# #OBS: '0' em ordem de CHAVE    '1' em ordem de VALOR
# ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# print(ranking)
# #
# #4ª_Imprime o ranking do maior para o menor
# print('-=' * 20)
# print('== RANKING DOS JOGADORES ==')
# for i, v in enumerate(ranking): #O enumerate não funciona com dicionario
#     print(f'{i+1}ª lugar: {v[0]} com {v[1]}')
  

from random import randint
from time import sleep
jogo = {}
from operator import itemgetter
while True:
    pessoa = randint(1, 5)

    if pessoa not in jogo:
        jogo['co_fa'] = pessoa

    if pessoa not in jogo:
        jogo['g_conte'] = pessoa

    if pessoa not in jogo:
        jogo['g_enga'] = pessoa

    if pessoa not in jogo:
        jogo['colab1'] = pessoa

    if pessoa not in jogo:
        jogo['colab2'] = pessoa
    if len(jogo) == 5:
        break
    
ranking = list()
print('Valor sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')
    sleep(0.5)