'''GUANABARA'''

'''Exercício Python 100: Faça um programa que tenha uma lista chamada números e 
duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los 
dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função 
anterior.'''

# from random import randint
# from time import sleep

# def sorteia(lista):
#     print('Sorteia 5 valores da lista: ', end='')
#     for cont in range(0, 5):
#         n = randint(1, 10)
#         lista.apppend(n)
#         print(f'{n} ', end='', flush=True)
#         sleep(0.3)
#     print('Pronto!')

# def somaPar(lista):
#     soma = 0
#     for valor in lista:
#         if valor % 2 == 0:
#             soma += valor
#     print(f'Somando os valores de {lista}, temos a {soma}')


# numeros = list()
# sorteia(numeros)
# somaPar(numeros)


from random import randint
from time import sleep

def nomes(valor):
    if valor == 1:
        numero1 = ' nome_do_numero1'
        print(numero1)
    elif valor == 2:
        numero2 = ' nome_do_numero2'
        print(numero2)
    elif valor == 3:
        numero3 = ' nome_do_numero3'
        print(numero3)
    elif valor == 4:
        numero4 = ' nome_do_numero4'
        print(numero4)
    elif valor == 5:
        numero5 = ' nome_do_numero5'
        print(numero5)


# sorteio = list()
# while True:
#     num = randint(1, 5)
#     if num not in sorteio:
#         sorteio.append(num)
    
#     if len(sorteio) == 5:
#         break

# print(sorteio)

# posicao = dict()
# posicao['co_facilitador']       = sorteio[0] 
# posicao['gestor_conhecimento']  = sorteio[1] 
# posicao['gestor_engajamento']   = sorteio[2] 
# posicao['colaborador 1']        = sorteio[3] 
# posicao['colaborador 2']        = sorteio[4] 

# for k, v in posicao.items():
#     print(k,'_', end='')
#     nomes(v)
#     # time.sleep(0, 5)

from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteado 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(0, 5)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0,3)
    print('PRONTO')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros = list()
sorteia(numeros)
somaPar(numeros)
