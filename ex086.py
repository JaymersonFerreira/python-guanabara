# coluna = []
# n = 0
# for cont in range(0, 3):
#     linha = []
#     for co in range(0, 3):
#         linha.append(int(input(f'Digite um número: [{n},{co}] ')))
#     n += 1
#     coluna.append(linha)
# print('-='*13)
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[ {coluna[l][c]} ]', end='')
#     print('')


'''GUANABARA'''
'''Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 
e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  #substituir esses monte de zeros por valores
for l in range(0, 3):                       #for da Linha
    for c in range(0, 3):                   #for da Coluna
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()                                 #toda vez que mostrar as colinas pula linha
