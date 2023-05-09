# num = [2, 5, 9, 1]#declaração da lista
# num[2] = 3        #substitui o 9 pelo 3
# num.append(7)     #adiciona no 7 como último elemento
# num.sort(reverse=True)   #ordena e reverte os números
# num.insert(2, 0)  #insere depois do 5 o valor 0
# num.pop()         #elemina o último elemento
# num.pop(2)        #elemina o 0 da lista
# num.remove(2)     #remove o elento 2
# if 5 in num:
#     num.remove(5)
# else:
#     print('Não cheio o número 4')
# print(num)
# print(f'Essa lista tem {len(num)} elementos.')


# valores = list()
# valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)

# for v in valores:
#     print(f'{v}...', end='')



'''Adcioinando apartir do teclado'''
# valores = list()
# for cont in range(0, 5):
#     valores.append(int(input(f'Digite {cont+1}ª a valor: ')))
#
# for c, v in enumerate(valores):
#     print(f'Na {c+1}ª posição encontrei o valor {v}!')
# print('Cheguei ao final da lista.')


'''Fazendo um aligação de uma lista'''
# a = [2, 3, 4, 7]
# b = a
# b[2] = 8
# print(f'Lista A: {a}')
# print(f'lista B: {b}')

'''Fazendo uma copia de uma lista'''
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'lista B: {b}')
'''
Lista A: [2, 3, 4, 7]
lista B: [2, 3, 8, 7]'''