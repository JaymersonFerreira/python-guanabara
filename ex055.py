# for c in range(0, 5):
#
#     peso = float(input('Peso: '))


maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de  {}Kg'.format(maior))
print('O maior peso lido foi de {}Kg'.format(menor))
