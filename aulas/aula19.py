pessoas = {'nome': 'Gustavi', 'sexo': 'M', 'idade': 22}
# print(pessoas['idade'])
'''22'''

# print(f'O {pessoas["nome"]} tem {pessoas["idade"]}')
'''O Gustavi tem 22'''

# print(pessoas.keys())
'''dict_keys(['nome', 'sexo', 'idade'])'''

# print(pessoas.values())
'''dict_values(['Gustavi', 'M', 22])'''

# print(pessoas.items())
'''dict_items([('nome', 'Gustavi'), ('sexo', 'M'), ('idade', 22)])'''

# for k in pessoas.keys():
#     print(k)
'''
nome
sexo
idade'''

# for k in pessoas.values():
#     print(k)
'''
Gustavi
M
22'''

# for k in pessoas.items():
#     print(k)
'''
('nome', 'Gustavi')
('sexo', 'M')
('idade', 22)'''

# del pessoas['sexo']
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
'''
nome = Gustavi
idade = 22'''

# pessoas['nome'] = 'Leandro'
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
'''
nome = Gustavi
idade = 22'''

# pessoas['peso'] = 98.5
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
'''
nome = Gustavi
sexo = M
idade = 22
peso = 98.5'''

# brasil = []
# estado1 = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil)           #uma lista com dicionarios
'''[{'uf': 'Rio de janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]'''

# print(brasil[0])
'''{'uf': 'Rio de janeiro', 'sigla': 'RJ'}'''

# print(brasil[1])
'''{'uf': 'São Paulo', 'sigla': 'SP'}'''

# print(brasil[0]['sigla'])
'''RJ'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
# for e in brasil:
#     for k, v in e.items():
#         print(f'O campo {k} tem o valor {v}.')
'''O campo uf tem o valor minas.
O campo sigla tem o valor mg.
O campo uf tem o valor acre.
O campo sigla tem o valor ac.
O campo uf tem o valor goias.
O campo sigla tem o valor go.'''

# for e in brasil:
#     for v in e.values():
#         print(v, end='')
#     print()
'''
MinasMG
GoíasGO
AcreAC'''