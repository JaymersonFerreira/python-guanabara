'''Crie um progrma que tennha um tupla totalmente preenchida com uma contagem por extenso,de zero ate vinte
Seu progrma deverá ler um número pelo teclado(ente 0 a 20) e mostrá-lo por extenso'''

# tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
#          'seis', 'sete', 'oito', 'nove', 'dez',
#          'onze', 'doze', 'treze', 'quatoze', 'quinze',
#          'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
# num = int(input('Digite um número: '))
# while 0 < num > 20:
#     num = int(input('Tente novamente. Digite um número: '))
# print(f'Você digitou {tupla[num]}')
'''Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, 
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

'''GANABARA'''
#cont recebe a as strings
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'quatoze', 'quinze',
         'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

núm = 0
while True:
    while True:
        núm = int(input('Digite um número entre 0 e 20: '))
        if 0 <= núm <= 20:      #Maior que 0 e menor que 20
            break
        print('Digite novamente. ', end='')
    print(f'Você digitou o número {cont[núm]}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break







