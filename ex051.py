# num = int(input('Primeiro: '))
# razao = int(input('razão: '))
# print(num, end=' -> ')
# for c in range(1, 10):
#     num = num + razao
#     print(num, end=' -> ')
# print('Acabou!!!')

'''GUANABARA'''
primeiro = int(input('primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end='-> ')
print('Acabou!!!')
