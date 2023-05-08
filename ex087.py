# matriz = []
# n = 0
# somaPares = 0
# somaColu = 0
# maior = 0
# manor = 0
# num = 0
# co = 0
# v = 0
# for cont in range(0, 3):
#     linha = []
#     for co in range(0, 3):
#         num = int(input(f'Digite um número: [{n},{co}] '))
#         linha.append(num)
#         if num % 2 == 0:
#             somaPares += num
#         if co == 2:
#             somaColu += num
#     n += 1
#     matriz.append(linha)
#     if cont == 1:
#         maior = max(matriz[1])
# print('-='*13)
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[ {matriz[l][c]} ]', end='')
#     print('')
# print(f'A soma dos Valores Pares: {somaPares}')
# print(f'Soma dos Valores da terceira coluna: {somaColu}')
# print(f'O maior da segunda linha: {maior}')

'''GUANABARA'''
'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  #substituir esses monte de zeros por valores
spar = maior = scol = 0
for l in range(0, 3):                       #for da Linha
    for c in range(0, 3):                   #for da Coluna
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()                                 #toda vez que mostrar as colinas pula linha
print('-=' * 30)
print(f'A soma dos valores é {spar}')
for l in range(0, 3):#for para pegar o elemento da terceira coluna
    scol += matriz[l][2]#a linha é vareavel e a coluna é fixa
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}.')


