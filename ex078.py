# valores = list()
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))
# for c, v in enumerate(valores):
#     print(f'Na posição {c}: {v}')
#
# print(f'O maior é o {max(valores)} e o menor {min(valores)}')
#

'''Exercício Python 079: Crie um programa onde o usuário possa
digitar vários valores numéricos e cadastre-os em uma lista.
   Caso o número já exista lá dentro, ele não será adicionado. No final,
serão exibidos todos os valores únicos digitados, em ordem crescente.'''

'''GUANABARA'''
# listanum = []
#
# mai = 0
# men = 0
# for c in range(0, 5):
#     listanum.append(int(input(f'Digite um valorpara a posição {c}: ')))
#     if c == 0: #quando 'c' for o primeiro listanum será o maior e o menor
#         mai = men = listanum[c]
#     else:
#         if listanum[c] > mai:
#             mai = listanum[c]
#         if listanum[c] < men:
#             men = listanum[c]
# print('=-' * 30)
# print(f'O maior valor digitado foi {mai} nas posições ', end='')
# for i, v in enumerate(listanum):
#     if v == mai:
#         print(f'{i}...', end='')
# print()
# print(f'O menor valor digitado foi {men} nas posições ', end='')
# for i, v in enumerate(listanum):
#     if v == men:
#         print(f'{i}...', end='')
# print()
listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append((int(input(f'Digite um valor para a Posição {c}: '))))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()
