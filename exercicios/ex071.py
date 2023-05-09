# saque = int(input('Que valor você quer sacar? R$')) #1234
#
# cinquenta = saque // 50 #24
# diferenca1 = cinquenta * 50 #1200
#
# vinte = (saque - diferenca1) // 20 #1
# diferenca2 = vinte * 20 #20
#
# dez = (saque - (diferenca1 + diferenca2)) // 10 #1
# diferenca3 = dez * 10 #10
#
# um = (saque - (diferenca1 + diferenca2 + diferenca3)) // 1 #4
#
# print(f'Total de {cinquenta} cédulas de R$50')
# print(f'Total de {vinte} cédulas de R$20')
# print(f'Total de {dez} cédulas de R$10')
# print(f'Total de {um} cédulas de R$1')


'''GUANABARA'''
# Verifica o mantante do dinheiro que é o 'total', vai tirando notas 50 reais até não dar mais,
# verifica o quanto sobrou e vai tirando notas de 20 até não dar mais,
# Verifica o quanto sobrou e vai tirando notas de 10 reais e por ultimo,
# verifica a quanto sobrou e vai tirando notas de 1 real.
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volta sempre ao BANCO CEV! Tenha um bom dia!')

