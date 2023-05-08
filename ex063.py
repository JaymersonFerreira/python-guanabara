# res = 0
# t1 = 0
# t2 = 1
# fim = 0
# print('\033[34m-----Sequência de Fibonacci-----\033[m')
# num = int(input('Sequência até: '))
#
# while num != fim <= num:
#     res = t1 + t2
#     t2 = t1
#     t1 = res
#     fim = t1 + t2
#     print(res, end='-> ')
#     if num == fim:
#         print(num, end='-> ')
# print('Acabou!!!')
# print('Fim do programa!')
# print(fim)

# print('_'*30)
# print('Sequecia de fibonacci')
# print('_'*30)
# n = int(input('Quantos termos você quer mostrar? '))
# t1 = 0
# t2 = 1
# print('~'*30)
# print('{} -> {}'.format(t1, t2), end='')
# cont = 3
# while cont <= n:
#     t3 = t1 + t2
#     print(' -> {}'.format(t3), end='')
#     t1 = t2
#     t2 = t3
#     cont += 1
# print(' -> FIM')












'''praticar'''
n = int(input('quantos mostrar: '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end=' -> ')
cont = 0
while cont <= n:
    t3 = t1 + t2
    print('{}'.format(t3), end=' -> ')
    t1 = t2
    t2 = t3
    cont += 1
print('Fim!')
