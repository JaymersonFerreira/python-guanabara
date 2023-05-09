# num = int(input('Primeiro: '))
# razao = int(input('razão: '))
# c = 1
# print(num, end=' -> ')
# while c != 10:
#     num = num + razao
#     print(num, end=' -> ')
#     c += 1
# print('Acabou!!!')
# escolha = 'S'
# while escolha != 'N':
#     mais = 0
#     escolha = str(input('\nQuer continuar?').upper())
#     mais = int(input('Quer mostrar mais quantos? '))
#     for c in range(0, mais):
#         num = num + razao
#         print(num, end=' -> ')
#     print('Acabou!!!')
#
# print('Fim do programa!!!')


'''GUANABARA'''
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= 10:
        print('{} -> .'.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
