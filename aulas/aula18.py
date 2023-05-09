# teste = list()
# teste.append('Gustavo')
# teste.append(40)
# print(teste)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(teste)

galera = [['João', 19], ['Joaquim', 33], ['Maria', 13], ['ana', 45]]
# print(galera[0][1])
'''19'''
# for p in galera:
#     print(p[1])
'''
19
13
13
45'''
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade.')
'''
João tem 19 anos de idade.
Joaquim tem 33 anos de idade.
Maria tem 13 anos de idade.
ana tem 45 anos de idade.'''


galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('nome: ')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear()
# print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é o mair idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')

