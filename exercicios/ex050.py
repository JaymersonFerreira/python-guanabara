# soma = 0
# for c in range(0, 3):
#     num = int(input('Digite um número: '))
#     if num % 2 == 0:
#         soma += num
# if soma == 0:
#     print('Todos os números são impares!')
# else:
#     print('Todos os numeros PARES somados é: {}'.format(soma))

'''GUANABARA'''

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} número e a soma foi {}'.format(cont, soma))
