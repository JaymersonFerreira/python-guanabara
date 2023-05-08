# preco = float(input('Preço: '))
# avista = preco - (preco * 10/100)
# avistaCartao = preco - (preco * 5/100)
# x3Cartao = preco + (preco * 20/100)
# print('À vista Dinheiro/Cheque: R${}'.format(avista))
# print('à vista cartão: R${}'.format(avistaCartao))
# print('Em até 2x no cartão: R${}'.format(preco))
# print('3x ou mais no cartão: R${}'.format(x3Cartao))

print('{:=^40}'.format(' LOJA GUANABARA '))
preco = float(input('Preco das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção '))
if opção == 1:
    total = preco - (preco * 10/100)
elif opção == 2:
    total = preco - (preco * 5/100)
elif opção == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} no final'.format(parcela))
elif opção == 4:
    total = preco + (preco * 20/100)
    totParc = int(input("quantas parcelas: "))
    parcela = total / totParc
    print('Sua compra de parcelada de {}x de R${:.2f} COM JURUS'.format(totParc, parcela))
else:
    total = preco
    print('\033[31mOPÇÃO INVÃLIDA DE PAGAMENTO!\033[m')
print('Sua compra de R${:.2f} vai custar {:.2f} no final.'.format(preco, total))
