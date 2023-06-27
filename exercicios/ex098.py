'''Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
'''
# from time import sleep

# def contador(i, f, p):
#     if p < 0:
#         p *= -1
#     if p == 0:
#         p = 1
#     print('-=' * 20)
#     print(f'Contagem de {i} até {f} de {p} em {p} ')
#     sleep(1.5)
#     if i < f:
#         cont = i
#         while cont <= f:
#             print(f'{cont} ', end='', flush=True)
#             sleep(0.3)
#             cont += p
#         print('FIM!')
#     else:
#         cont = i
#         while cont >= f:
#             print(f'{cont} ', end='', flush=True)
#             sleep(0.3)
#             cont -= p
#         print('FIM!')

# #Programa Principal
# contador(1, 10, 1)
# contador(10, 0, 2)

# print('-=' * 20)
# print('Agora é sua vez de personalizar a contagem!')
# ini = int(input('Inicio:    '))
# fim = int(input('Fim:       '))
# pas = int(input('Passo:     '))
# contador(ini, fim, pas)

from time import sleep

#função
def contador(i, f, p):
    #caso o "passo" seja negativo ou 0
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print('-=' * 20)
    print(f'Contador de {i} até {f} de {p} em {p}')
    sleep(0.3)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('Fim!')
    else: 
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('Fim!')

#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
