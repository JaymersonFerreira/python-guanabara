def escreva(txt):
    t = len(txt) + 10

    print('~' * t)
    print(f'{txt:^{t}}')
    print('~' * t)


texto = str(input('Escreva alguma coisa: '))
escreva(texto)


'''GUANABARA'''
'''Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.'''

# def esreva(msg):
#     tam = len(msg) + 4
#     print('~' * tam)
#     print(f'  {msg}')
#     print('~' * tam)
#
# # Programa Pricipal
# escreva('Gustavo Guanabara')
# esreva('Curso de Python no YouTube')
# esreva('CeV')