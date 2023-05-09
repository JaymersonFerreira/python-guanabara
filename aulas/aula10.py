# nome = str(input('Qual o seu nome?'))
# if nome == 'Jaymerson':
#     print('Que nome lindo você tem!')
# else:
#     print('Seu nome é tão normal!')
# print('Bom dia {}!'.format(nome))


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi {:.2f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa, PAREBENS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
# print('PARABENS' if m >= 6 else 'ESTUDE MAIS!')
