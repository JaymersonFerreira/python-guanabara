# num1 = int(input('Digite dois números\nDigite o 1ª número: '))
# num2 = int(input('Digite o 2ª número: '))
# escolha = 0
# while escolha != 5:
#     print('-----MENU-----\n'
#           '[ 1 ] somar\n'
#           '[ 2 ] multiplicar\n'
#           '[ 3 ] maior\n'
#           '[ 4 ] novos numeros\n'
#           '[ 5 ] sair do programa')
#     escolha = int(input('O que deseja fazer: '))
#     if escolha != 5:
#         if escolha == 1:
#             soma = num1 + num2
#             print('A soma é: {}'.format(soma))
#
#         elif escolha == 2:
#             mult = num1 * num2
#             print('A multiplicação é: {}'.format(mult))
#
#         elif escolha == 3:
#             if num1 > num2:
#                 print('O 1ª número: {}, é maior que o 2ª número: {}.'.format(num1, num2))
#             elif num1 < num2:
#                 print('O 2ª número: {}, é maior que o 1ª número: {}.'.format(num2, num1))
#             else:
#                 print('O números são iguais!')
#         elif escolha == 4:
#             num1 = int(input('Digite o 1ª número: '))
#             num2 = int(input('Digite o 2ª número: '))
#         elif escolha == 5:
#             escolha = 5
#         else:
#             print('Opção incorreta!!!\nTente Novamente...')
#
# print('Fim do programa!')

'''GUANABARA'''

from time import sleep
n1 = int(input('Primeira valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:

    print('''    [ 1 ]
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('Qual é o sua opção?'))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} * {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))

    elif opção == 4:
        print('Informe os número novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa!')
