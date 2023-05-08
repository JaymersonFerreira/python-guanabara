'''Desenvolva um progrma que leia quatro valres pelo teclado e
guarde-os em uma tupla. No final mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais Foram os Números Pares'''

# primeiro = int(input('Primeiro número: '))
# segundo = int(input('Segundo número: '))
# terceiro = int(input('Terceiro número: '))
# quarto = int(input('Quarto número: '))
#
# cont = 0
# tupla = (primeiro, segundo, terceiro, quarto)
# print(f'O 9 aparece {tupla.count(9)} vezes')
# if 3 in tupla:
#     print(f'O 3 aparace na {tupla.index(3)+1}ª posição')
# else:
#     print('O 3 não foi digitado!')
#
#
# if tupla[0] % 2 == 0:
#     print('O Primeiro é Par')
# if tupla[1] % 2 == 0:
#     print('O Segundo é Par')
# if tupla[2] % 2 == 0:
#     print('O Terceiro é Par')
# if tupla[3] % 2 == 0:
#     print('O Quarto é Par')
# if tupla[0] % 2 == 1 and tupla[1] % 2 == 1 and tupla[2] % 2 == 1 and tupla[3] % 2 == 1:
#     print('Não foi digitado número Par')
'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

'''GUANABARA'''

núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores: {núm}')
print(f'o valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:    #se 3 estiver dentro de num
    print(f'O valor 3 apareceu na {núm.index(3)+1}ª posição')   #mostra a posição do primeiro 3
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitos foram ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')
