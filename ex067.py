#
# while True:
#     c = 0
#     resp = 0
#     print('-' * 30)
#     valor = str(input('Quer ver a tabuada de qual valor? '))
#     print('-' * 30)
#
#     if valor[0] == '-':
#         break
#     while c < 10:
#         c += 1
#         resp = int(valor) * c
#         print(f'{valor} x {c} = {resp}')
# print('Fim do programa!')


'''GUANABARA'''

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('fim do programa: ')