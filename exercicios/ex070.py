# total = maisMil = menorProduto = menorValor = 0
# continuar = 'S'
# n = 0
# nomeP = ''
#
# while True:
#     if continuar == 'N':
#         break
#     if continuar == 'S':
#         produto = str(input('Nome do produto: '))
#         valor = float(input('Preço: R$'))
#
#         if menorProduto >= valor:
#             menorValor = valor
#             nomeP = produto
#
#         if valor >= 1000:
#             maisMil += 1
#
#         total += valor
#
#         while True:
#             continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
#             if continuar == 'S' or continuar == 'N':
#                 break
# print(f'O total da compra foi R${total}')
# print(f'temos {maisMil} produtos custando mais de R$1000.00')
# print(f'O produto mais bataro foi {nomeP} que custa R${menorValor}')

'''guanabara'''
# total = totmil = menor = cont = 0
# barato = ' '
# while True:
#     produto = str(input('Produto: '))
#     preco = float(input('Preco: R$'))
#     cont += 1
#     total += preco
#     if preco >= 1000:
#         total += 1
#     if cont == 1 or preco < menor:
#         menor = preco
#         barato = produto
#     resp = ' '
#     while resp not in 'SN':
#         resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
#     if resp == 'N':
#         break
# print('{:-^40}'.format(' FIM DO PROGRAMA '))
# print(f'O total da compra foi R${total:.2f}')
# print(f'Temos {total} produtos custando mais de R$1000.00')
# print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

'''exercicio'''
barato = total = maisMil = cont = 0
nomeBarato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = int(input('Preço: R$'))
    total += preco
    cont += 1
    if preco >= 1000:
        maisMil += 1
    if cont == 1 or barato > preco :
        barato = preco
        nomeBarato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]'))
    if resp == 'N':
        break
print(f'Total gasto {total}')
print(f'{maisMil} produtos acima de R$1000,00')
print(f'O produto mais barato é: {nomeBarato} que vale: {barato}')

