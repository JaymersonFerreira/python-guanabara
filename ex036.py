# casa = float(input('Valor da casa: '))
# salario = float(input('Salario: '))
# tempo = int(input('Tempo: '))
#
# limite = salario * 30/100
#
# tempo = tempo * 12
# prest = casa / tempo
# print('As prestações mensais ficaram em: \033[1;34mR${:.2f}\033[m'.format(prest))
#
# if prest > limite:
#     print('\033[31;1mNão é possível fazer o empréstimo!\033[m \033[33mPagamento mensal acima de 30% do salario.\033[m')
# elif prest < limite:
#     print('\033[32mTudo certo!! É possível fazer o emprestimo:\033[m')


'''Guanabara'''

casa = float(input('Valor da casa: R$'))
salario = float(input('Salário da comprador: R$'))
anos = int(input('quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar um casa de R${}:.2f em {} anos'.format(casa, anos), end='')
print(' a prestação sera de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
