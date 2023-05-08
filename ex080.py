# valores = []
# ultimo = 0
# for c in range(0, 5):
#     num = int(input('Digite um número: '))
#     if num <= ultimo:
#         valores.insert(0, num)
#         print('Adicionado na primeira posição')
#     if c == 0 or num > ultimo:
#         valores.append(num)
#         ultimo = num
#         print('Adicionado na última posição')
#
#
# print(valores)

'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

# lista = list()
# for c in range(0, 5):
#     n = int(input('Digite um valor: '))
#     if c == 0 or n > lista[-1]: #Vai da um append se for o primeiro ou foi maior do que o último valor #[-1] final
#         lista.append(n)
#         print('Adicionado ao final da lista...')
#     else: #Vai varrer o vetor
#         pos = 0
#         while pos < len(lista): #Vai da primeira posição a última posição
#             if n <= lista[pos]: #Verifica se o número que eu quero inserir é menor do que ja esta na lista[pos]
#                 lista.insert(pos, n)
#                 print(f'Adicionado na posição {pos} da lista')
#                 break
#             pos += 1
# print('-=' * 30)
# print(f'Os valores digitados em ordem foram {lista}')

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionar ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionar na posição {pos} dalsita...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
