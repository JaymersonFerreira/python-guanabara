print('\033[33mDigite dois números...\033[m')
primeiro = int(input('Primeiro número: '))
segundo = int(input('Segundo número: '))
if primeiro > segundo:
    print('\033[34mO primeiro é maior!\033[m')
elif primeiro < segundo:
    print('\033[34mO segundo é maior!\033[m')
else:
    print('\033[34mOs dois são iguais!\033[m')
