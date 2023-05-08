# l1 = int(input('Primeiro lado: '))
# l2 = int(input('Segundo lado: '))
# l3 = int(input('Terceiro lado: '))
#
# if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l2 > l1:
#     print('Essas medidas formam um trianfulo!')
#     if l1 == l2 and l1 == l3 and l2 == l3: #L1 == L2 == L3
#         print('E um triangulo equilátero!')
#     elif l1 != l2 and l2 != l3 and l2 != l3: #l1 != l2 != l3 != l3 != l1
#         print('É um triangulo escaleno!')
#     elif l1 == l2 or l1 == l3 or l2 == l3:
#         print('É um triangulo isosceles!')
# else:
#     print('Essas medidas não formam um triangulo!')


'''Gauanabara'''

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r3:
    print('Os segmentos acima PODEM FORMAR em TRIANGULO!')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NAO PODEM FORMAR TRIANGULO')