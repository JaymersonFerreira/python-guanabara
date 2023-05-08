# import datetime
# data = datetime.date.today()
# data = data.strftime('%Y')
# ano = int(data)
#
# nasc = int(input('Ano de nascimento: '))
#
# result = ano - nasc
#
# if result <= 9:
#     print('\033[34mPossui {} anos. MIRIN!!!\033[m'.format(result))
# elif 10 < result < 14:
#     print('\033[34mPossui {} anos. INFATIL!!!\033[m'.format(result))
# elif 15 < result < 19:
#     print('\033[34mPossui {} anos. JUNIOR!!!\033[m'.format(result))
# elif result == 20:
#     print('\033[34mPossui {} anos. SÊNIOR!!!\033[m'.format(result))
# elif result > 20:
#     print('\033[34mPossui {} anos. MASTER!!!\033[m'.format(result))


'''Guanabara'''
from datetime import date

atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIN')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
