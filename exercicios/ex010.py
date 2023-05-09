n = float(input('Quantos reais você tem? R$'))
emDolar = n / 3.27
print('É possivel comprar US${:.2f} com R${:.2f}'.format(emDolar, n))