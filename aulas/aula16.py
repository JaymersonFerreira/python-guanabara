# lanche = () [] {}     ()->Tuplas []->Listas {}->Dicionario

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# print(lanche)
'''('Hamburguer', 'Suco', 'Pizza', 'Pudim')'''
# print(lanche[1])
'''Suco'''
# print(lanche[-2])
'''Pizza'''
# print(lanche[1:3]) inicia no 'Suco' e termina na 'Pizza'
'''('Suco', 'Pizza')'''
# print(lanche[2:]) inicia na ('Pizza') e vai até o final
'''('Pizza','Pudim')'''
# print(lanche[:2]) inicia no 'Hamburguer' e termina no 'Suco', a ('Pizza')[2] é ignorada
'''('Hamburguer', 'Suco')'''
# print(lanche[-3:]) inicia no 'Suco' e vai até o final 'Pudim'
'''('Suco','Pizza', 'Pudim')'''

# ____________________
# Tuplas são imutáveis
# --------------------
# lanche[1] = 'Refrigerante'
# print(lanche[1])


# for comida in lanche:
#     print(f'Eu vou comer {comida}')
# print('Comi para caramba!')

# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
# print(len(lanche))
# print('Comi para caramba!')


# for cont in range(0, len(lanche)):
#     print(cont)

# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]}')
# print('Comi pra caramba!')

# for cont in range(0, len(lanche)): #/ para mostar a posição
#     print(f'Eu vou comer {lanche[cont]} na posição {cont}')
# print('Comi pra caramba!')

# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
# for pos, comida in enumerate(lanche): # tanto o 'pos' e 'comida' vão de 0 a 5, mas o 'comida' esta ligada ao enumerate(lanche)
#     print(f'Eu vou comer {comida} na posição {pos}')
# print('Comi pra caramba!')

# ---------------------------------------------------------------------------------
# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
#
# for comida in lanche: # é a maneira mais simple, se não precisar mostrar a posição
#     print(f'Eu vou comer {comida}')
#
# for cont in range(0, len(lanche)): #se precisar mostrar a posição com o range()
#     print(f'Eu vou comer {lanche[cont]} na posição {cont}')
#
# for pos, comida in enumerate(lanche): #se precisar mostrar a posição, mas tem q colocar duas vareaveis no for
#     print(f'Eu vou comer {comida} na posição {pos}')
# print('Comi pra caramba!')
# --------------------------------------------------------------------------------------

# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
# print(sorted(lanche)) # coloca em ordem, transforma em LISTA
# print(lanche)


# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = a + b # vai juntar a e b
# print(c)
'''(2, 5, 4, 5, 8, 1, 2)'''

# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = a + b
# print(c)
# print(len(c))# vai contar quantos elementos tem o 'c'
'''(2, 5, 4, 5, 8, 1, 2)
2'''

# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = a + b
# print(c)
# print(c.count(5))# conta quantas vezes o 5 aparece
'''(2, 5, 4, 5, 8, 1, 2)
2'''

# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = a + b
# print(c)
# print(c.index(8))# Verifica onde estar o numero 8, e so pega a primeira ocorrencia
'''(2, 5, 4, 5, 8, 1, 2)
4'''


# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = b + a
# print(c)
# print(c.index(5))# Verifica onde estar o numero 5, iniciando na posição 1, e so pega a primeira ocorrencia
'''(5, 8, 1, 2, 2, 5, 4)
0'''

'''as tuplas podem receber dados de tipos deferentes'''
# pessoa = ('Gustavo', 39, 'M', 99.88)
# print(pessoa)
'''('Gustavo', 39, 'M', 99.88)'''

# pessoa = ('Gustavo', 39, 'M', 99.88)
# del(pessoa)# apaga da memoria
# print(pessoa)

# pessoa = ('Gustavo', 39, 'M', 99.88)
# del(pessoa[0]) #Não permite apagar elementos dentro da tupla, já que são imutáveis
# print(pessoa)

Squad 5
Jaymerson
Lucas
Jefferson
Aron
Joel Gomes