# sexo = 0
# while sexo != 'M' and sexo != 'F':
#     sexo = str(input('Qual o seu sexo: ')).upper()
# print('\033[34mFim!')

'''GUANABARA'''

sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registado com sucesso'.format(sexo))

