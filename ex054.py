# from datetime import date
# atual = date.today().year
# maior = 0
# menor = 0
# for c in range(0, 7):
#     dataNasc = int(input('Data de nascimento: '))
#     ano = atual - dataNasc
#     if ano >= 18:
#         maior += 1
#     else:
#         menor += 1
# print('{} pessoas são maiores de idade'.format(maior))
# print('{} pessoas são menores de idade'.format(menor))

'''GUANABARA'''
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maires de idade'.format(totmaior))
print('E tambem tivemos {} pessoas menores de idade'.format(totmenor))
