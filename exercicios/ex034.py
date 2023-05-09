salario = float(input('Salario: R$'))
if salario >= 1250:
    almento = salario + (salario * 10/100)
    print('O salario de {} teve um almento de 10%, ficou {}'.format(salario, almento))
else:
    almento = salario + (salario * 15/100)
    print('O salario de {} teve um almento de 15%, ficou {}'.format(salario, almento))