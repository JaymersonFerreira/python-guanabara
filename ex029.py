velocidade = int(input('Qual velocidade: '))
if velocidade <= 80:
    print('Não recebeu multa!')
else:
    multa = (velocidade - 80) * 7
    print('Pagara uma multa de R${}'.format(multa))

velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permite que é de 80km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')