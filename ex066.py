# cont = soma = 0
# while True:
#     num = int(input('Digite um número: (999) para parar): '))
#     if num == 999:
#         break
#     soma += num
#     cont += 1
# print(f'A soma é {soma} e foram digitados {cont} números.')

'''GUANABARA'''

num = cont = soma = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos valores foi {soma}!')
