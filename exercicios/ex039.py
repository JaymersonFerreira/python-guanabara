# import datetime
#
# date = datetime.date.today()
# year = date.strftime('%Y')
#
# nasc = int(input('Digite o ano do seu nascimento: '))
# result = int(year) - nasc
#
# if result < 0:
#     print('Você ainda não nasceu!!!')
# elif 0 < result < 17:
#     print('Sua idade é: {} anos. Ainda não vai se alista ao serviço militar!!!'.format(result))
# elif result == 17:
#     print('Sua idade é: {} anos. É a hora de se alistar!!!'.format(result))
# elif 17 > result > 20:
#     print('Sua idade é: {} anos. Já possou o tempo de se alistar!!!'.format(result))
# else:
#     print('\033[31mMuito velho para se alistar!!!\033[m')


'''Guanabara'''



from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu a listamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))