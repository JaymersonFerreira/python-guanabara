# lista = []
# pares = []
# impares = []
# for i in range(0, 7):
#     num = int(input(f'Digite {i+1}ª número: '))
#     if num % 2 == 0:
#         pares.append(num)
#     else:
#         impares.append(num)
# pares.sort()
# impares.sort()
# lista.append(pares[:])
# lista.append(impares[:])
# print(f'Os valores pares digitados foram: {lista[0]}')
# print(f'Os valores ímpares digitados foram: {lista[1]}')
# print(lista)

'''GUANABARA'''

num = [[], []]                  #criar listas dentro de uma lista
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}ª. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)    #na primeira posição da lista 'num' adicione valor
    else:
        num[1].append(valor)    #na segunda posição da lista 'num' adicione valor
print('-='*30)
num[0].sort()                   #ordena em ordem crecente
num[1].sort()                   #ordena em ordem crecente
print(f'Os valore pares digitados foram: {num[0]}')
print(f'Od valores impares digitados foram: {num[1]}')
