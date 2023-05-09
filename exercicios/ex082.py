# lista = []
# listaPar = []
# listaImpar = []
# while True:
#     num = int(input('Digite um número: '))
#     lista.append(num)
#     if num % 2 == 0:
#         listaPar.append(num)
#     else:
#         listaImpar.append(num)
#     resp = str(input('Quer continuar? [S/N] '))
#         if resp in 'Nn':
#             break

# print('lista: {}'.format(lista))
# print(f'lista Par: {listaPar}')
# print(f'lista impar: {listaImpar}')

'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
   Depois disso, crie duas listas extras que vão conter apenas os valores pares e os
valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''

'''GUANABARA'''

# num = list()
# pares = list()
# impares = list()
# while True:
#     num.append(int(input('Digite um número: ')))
#     resp = str(input('Quer continuar? [S/N] '))
#     if resp in 'Nn':
#         break
# for i, v in enumerate(num):
#     if v % 2 == 0:
#         pares.append(v)
#     elif v % 2 == 1:
#         impares.append(v)
# print('-=' * 30)
# print(f'A lista completa é {num}')
# print(f'A lista de pares é {pares}')
# print(f'A lista de ímpares é {impares}')

num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digitou um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
