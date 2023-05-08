distacia = int(input('Qual a distacia da viagem em KM: '))
'''pagar = distacia * 0.50 if distacia <= 200 else distacia * 0.45'''
if distacia <= 200:
    pagar = distacia * 0.5
    print('Vai pagar R${:.2f}'.format(pagar))
else:
    pagar = distacia * 0.45
    print('Vai pagar R${:.2f}'.format(pagar))

