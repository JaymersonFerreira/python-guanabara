# n = int(input('Digite um número para a tabuada: '))
# for c in range(1, 11):
#     mult = c * n
#     print('{}X{}={}'.format(n, c, mult))

'''GUANABARA'''
num = int(input('Digite um número para ver a tabuada: '))
for c in range(1, 11):
    print('{} X {:2} = {}'.format(num, c, num*c))
