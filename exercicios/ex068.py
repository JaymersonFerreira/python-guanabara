# from random import randint
# cont = 0
# while True:
#     par = 'Par'
#     impar = 'Impar'
#     fim = False
#     result = 0
#     pc = randint(1, 10)
#     print('=' * 45)
#     vc = int(input('Escolha um número: '))
#     escolha = str(input('você vai escolher Par[P] ou Impar[I]? ').upper().strip()[0])
#     print(f'Você escolheu: \033[32m{vc}\033[m e o pc sorteou: \033[32m{pc}\033[m\033[m')
#     resto = (pc + vc) % 2
#     if resto == 0:
#         parOuImpar = par
#         result = par
#     else:
#         parOuImpar = impar
#         result = impar
#     if escolha == 'P' and parOuImpar == par or escolha == 'I' and parOuImpar == impar:
#         print(f'\033[32mParabens você venceu!!!\033[m O resultado foi \033[36m{result}\033[m')
#         print('=' * 45)
#         cont += 1
#     else:
#         print(f'\033[31mVocê Perdeu!!!\033[m O resultado foi \033[36m{result}\033[m')
#         print('=' * 45)
#         fim = True
#     if fim == True:
#         break
# print(f'\033[34mVocê venceu\033[m \033[32m{cont}\033[m \033[34mvezes\033[m')


'''Guanabara'''

# from random import randint
# v = 0
# while True:
#     jogador = int(input('Diga um valor: '))
#     computador = randint(0, 10)
#     total = jogador + computador
#     tipo = ' '
#     while tipo not in 'PI':
#         tipo = str(input('Par ou Ímpar ')).strip().upper()[0]
#     print(f'Você jogou {jogador} e o computador {computador}. total de {total}', end='')
#     print('DEU PAR if' if total % 2 == 0 else 'DEU IMPAR')
#     if tipo == 'P':
#         if total % 2 == 0:
#             print('Você VENCEU!!')
#             v += 1
#         else:
#             print('Você PERDEU!')
#             break
#     elif tipo == 'I':
#         if total % 2 == 1:
#             print('Você VENCEU!')
#             v += 1
#         else:
#             print('Você PERDEU!')
#             break
#     print('Vamos jogar novamente...')
# print(f'GAME OVER! Você venceu {v} vezes.')



from random import  randint
v = 0
while True:
    jogador = int(input('Esclha um número?'))
    computador = randint(1, 5)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você escolhe PAR OU IMPAR?')).upper().strip()[0]
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!!!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu?!!!')
            v += 1
        else:
            print('Você PERDEU!!!')
            break
    print('Vamos jogar de novo!!!')
print(f'Você ganhou {v} vezes ')

