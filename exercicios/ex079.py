# valores = []
# while True:
#     num = int(input('Digite um número: '))
#     if num in valores:
#         print('\033[31mValor ja inserido.\033[m')
#     while num not in valores:
#         valores.append(num)
#     resp = ' '
#     while resp not in 'SN':
#         resp = str(input('Quer coninuar? [S/N] ')).upper().strip()[0]
#     if resp == 'N':
#         break
#     lista = valores.sort()
# print('Você digitou os valores: {}'.format(lista))

'''GUANABARA'''

# numeros = list()
# while True:
#     n = int(input('Digirte um valor: '))
#     if n not in numeros: #Confere se tem 'n' dentro da lista 'numeros'
#         numeros.append(n)
#         print('Adicionado com com sucesso...')
#     else:
#         print('Valor duplicado! Não vou adicionar...')
#
#     r = str(input('Quer continuar? [S/N] '))
#     if r in 'Nn':
#         break
# print('-=' * 30)
# numeros.sort()
# print(f'Você digitou  os valores {numeros}')


numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com suceso...')
    else:
        print('Valor duplicado! não cou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('=-' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}')
