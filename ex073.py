'''Crie uma tupla preenchida com os
20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

# times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthias', 'Flamengo', 'Atletico-PR', 'Atlético-MG', 'Fotaleza',
# 'São Paulo', 'América', 'Botafogo', 'Santos', 'Santos', 'Goiás', 'Bragatino', 'Coritiba', 'Ceara', 'Atletico-GO', 'Avaí', 'Juventude')
# print(times[:5])
# print(times[-4:])
# print(sorted(times))
# print(times.index('Flamengo')+1)
'''Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de 
Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.'''

'''GUANABARA'''
times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthias',
         'Flamengo', 'Atletico-PR', 'Atlético-MG', 'Fotaleza',
         'São Paulo', 'América', 'Botafogo', 'Santos', 'Santos',
         'Goiás', 'Bragatino', 'Coritiba', 'Ceara', 'Atletico-GO',
         'Avaí', 'Juventude')
print('-=' * 10)
print(f'Lista de times do Brasileirão: {times}') #imprime tudo
print('-=' * 10)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 10)
print(f'Os 4 últimos são {times[-4:]}') #pego do quarto ultimo até o final
print('-=' * 10)
print(f'Times em ordem alfabética: {sorted(times)}')    #ordem alfabetica
print('-=' * 15)
print(f'O Flamenfo está na {times.index("Flamengo")+1}ª posição')   #o index mostra onde estar localizado, mais pq a primeira é o 0
