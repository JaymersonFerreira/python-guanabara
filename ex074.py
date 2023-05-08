'''Crie um programa que vai gerar cinco números aleatórios
e colocar em uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o maior valor que
estão na tupla'''
'''tuplas = coleções'''
from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
            randint(1, 10), randint(1, 10))             #insere numeros aleatorios direto na tupla
print('Os valores sorteados foram: ', end='')
for n in numeros:                                       #pega do primeiro número sorteado até o último
    print(f'{n}', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')   #analisa o maior número sorteado
print(f'O menor valor sorteado foi {min(numeros)}')     #analiza o menor número sorteado

