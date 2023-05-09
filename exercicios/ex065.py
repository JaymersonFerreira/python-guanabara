'''GUANABARA'''
# resp = 'S'
# soma = quant = media = maior = menor = 0
# while resp in 'Ss':
#     num = int(input('Digite um número: '))
#     soma += num
#     quant += 1
#     if quant == 1:
#         maior = menor = num
#     else:
#         if num > maior:
#             maior = num
#         if num < menor:
#             menor = num
#
#     resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
# media = soma / quant
# print('Você digitou {} de numeros e a média foi {}'.format(quant, media))
# print('O maior valor foi  {} e o menor foi {}'.format(maior, menor))


'''PRATICAR'''
soma = cont = quant = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    cont += 1
    if quant == 1:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    resp = str(input('Deseja continuar: ').upper().strip()[0])
media = soma / cont
print('A soma foi {} e a media foi {:.2f}'.format(soma, media))
print('O maior foi {} e o menor foi {}'.format(maior, menor))
