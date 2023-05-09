n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print('O MAIOR número foi: {}'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O MAIOR número foi: {}'.format(n2))
else:
    print('O MAIOR número foi: {}'.format(n3))

if n1 < n2  and n1 < n3:
    print('O MENOR numero foi: {}'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O MENOR número foi: {}'.format(n2))
else:
    print('O MENOR número foi: {}'.format(n3))

    #--------------------------------------#

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))


