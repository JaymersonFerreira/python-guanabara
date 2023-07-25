def aumentar(preco=0, taxa=0, formato=False):
    '''
    -> Calcula o aumento de um determinado preço
    retornando o resultado com ou sem formatação.
    :param preco: o preço que se quer reajustar.
    :param taxa: qual a é a porcentagem de aumento.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado,  com ou sem formato.
    '''
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=0):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=0):
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(3))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço,taxaa, True)}')
    print(f'{taxar}% de redução: \t\t{diminuir(preço, taxar, True)}')
    print('-' * 30)

