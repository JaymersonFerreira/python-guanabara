# lista = list()
# cont = 0
# while True:
#     cont += 1
#     lista = input('Digite um numero: ')
#     resp = ' '
#     while resp not in 'SN':
#         resp = str(input('Quer continuar? [S/N] ')).upper().strip()
#     if resp == 'N':
#         break
# print(f'Foram digitados {cont} números.')
# if lista in 5:
#     print('O número 5 foi digitado, o primeiro 5 esta na posição {}'.format(lista.index(5)))
# else:
#     print('O número 5 não foi digitado')
# print(f'{lista.sort(reverse=True)}')
#
'''GUANABARA'''
'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

# valores = []
# while True:
#     valores.append(int(input('Digite um valor: ')))
#     resp = str(input('Quer continuar? [S/N] '))
#     if resp in 'Nn':
#         break
# print('-=' * 30)
# print(f'Você digitou {len(valores)} elementos')
# valores.sort(reverse=True)
# print(f'Os valores em ordem decrescente são {valores}')
# if 5 in valores: #Procura dentro da valores[] se tem o núemro 5
#     print('O valor 5 faz parte da lista')
# else:
#     print('O valor 5 não foi encontrado na lista!')

valores = []
while True:
    valores.append((int(input('Digite um valor: '))))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrecente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
