listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.00,
            'Estojo', 25,
            'Tranferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Caneta', 22.30,
            'Livro', 34.90)
print('-' * 40)
print(f'\033[44m{"LISTAGEM DE PREÇO":^40}\033[m')
print('-' * 40)
for pos in range(len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)
