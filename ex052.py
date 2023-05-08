# num = int(input('numero primo: '))
#
# if 2 <= num == num  / 1 and num // num == 1:
#     print('Número primo!')
# else:
#     print('não é número primos!')

'''GUANABARA'''

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '. format(c), end='')
print('\n\033[mO númeo {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')

