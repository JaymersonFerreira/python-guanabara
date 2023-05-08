# '''GUANABARA'''
# '''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.'''
# jogador = dict()
# partidas = list()
# #Divido em 7 partes
# #1ª_Coleta do nome e total de partidas
# jogador['nome'] = str(input('Nome do Jogador: '))
# tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
# #2ª_Coleta da quantidade de gols de cada partida
# for c in range(0, tot):
#     partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
# #3ª_Cria uma copia da lista 'partidas' com os gols
# jogador['gols'] = partidas[:]
# jogador['total'] = sum(partidas)    #soma o total de gols de 'partidas'
# #4ª_Imprime o dicionario 'jogador'
# print('-=' * 30)
# print(jogador)
# print('-=' * 30)
#5ª_Imprime a chave e o valor de jogador.itens()
# for k, v in jogador.items():
#     print(f'O campo {k} tem o valor {v}')
# print('-=' * 30)
# #6ª_Imprime o total de gols feitos pelo jogador
# print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
#7ª_Imprime a chabe e o valor de jogador.itens()
# for i, v in enumerate(['gols']):
#     print(f'    => Na partida {i}, fez {v} gols')

jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome: '))
tot = int(input('Quantidade de partidas: '))
for c in range(0, tot):
    partidas.append(int(input(f'Gols no {c+1} jogo: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)
for k, v in jogador.items():
    print(f'Na chave {k} possuo o valor {v}')
for i, j in enumerate(jogador['gols']):
    print(f'No {i}ª jogo foram feitos {j} gols pelo {jogador["nome"]}')