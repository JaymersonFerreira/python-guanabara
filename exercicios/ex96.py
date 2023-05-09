# def area(l, c):
#     mult = l * c
#     print(mult)
#
# largura = float(input('Largura (m): '))
# comprimetno = float(input('Comprimento (m): '))
#
# area(largura, comprimetno)

'''GUANABARA'''
'''Exercício Python 096: Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def area(larg, comp):
    a = larg * comp
    print(f'Aarea de um terreno {larg}X{comp} é de {a}m²')

# Programa principal
print(' Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (M): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)