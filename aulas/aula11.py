# print('\033[7 ;33;44mOlá, mundo!\033[m')

# a = 5
# b = 3
# print('Os valores são \033[32m{} \033[me \033[31m{}\033[m'.format(a, b))

# nome = 'jayme'
# print('Muito prazer em te conhecer {}{}{}'.format('\033[4;34m', nome, '\033[m'))

nome = 'jayme'
cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'pretoebranco': '\033[7;30m'
}
print('Muito prazer em te conhecer {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa']))
