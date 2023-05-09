l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    print('Essas medidas formam um triangulo!')
else:
    print('Essas medidas não formam um triangulo!')
