num = int(input('Primeiro: '))
razao = int(input('razão: '))
print(num, end=' -> ')
for c in range(1, 10):
    num = num + razao
    print(num, end=' -> ')
print('Acabou!!!')
escolha = 'S'
while escolha != 'N':
    mais = 0
    escolha = str(input('\nQuer continuar? [S/N]: ').upper())
    if escolha == 'S':
        mais = int(input('Quer mostrar mais quantos? '))
        for c in range(0, mais):
            num = num + razao
            print(num, end=' -> ')
        print('Acabou!!!')
    else:
        print('Opção inválida!')

print('Fim do programa!!!')



'''for GUANABARA'''
# primeiro = int(input('primeiro termo: '))
# razão = int(input('Razão: '))
# décimo = primeiro + (10 - 1) * razão
# for c in range(primeiro, décimo + razão, razão):
#     print('{} '.format(c), end='-> ')
# print('Acabou!!!')


'''GUANABARA'''
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA'))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> .'.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')
