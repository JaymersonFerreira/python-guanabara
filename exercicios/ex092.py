'''GUANABARA'''
'''Exercício Python 092: Crie um programa que leia nome, 
ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
# from datetime import datetime
# #Dividdo em 3 partes
# #1ª_Coleta de dados e armazenado no dicionário
# dados = dict()
# dados['nome'] = str(input('Nome: '))
# nasc = int(input('Ano de nascimento: '))
# dados['idade'] = datetime.now().year - nasc
# dados['ctps'] = int(input('Carteira de trabalho (0 não tem) '))
# #2ª_Se o valor em dados['ctps'] for diferente de 0, coleta mais alguns dados sobre a ctps
# if dados['ctps'] != 0:
#     dados['contratação'] = int(input('Ano de Contratação: '))
#     dados['salario'] = float(input('Salário: R$'))
#     dados['aposentadira'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
# print(dados)
# #3ª_Impreção dos dados
# for k, v in dados.items():#para cada key e values em dados.itens()
#     print(f'    - {k} tem o valor {v}')

dados = {}
from datetime import datetime
dados['nome'] = str(input('Nome: '))
nasc = int(input('Data de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho: [0 caso nao tenha] '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Data de contratação: '))
    dados['salario'] = int(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
for k, v in dados.items():
    print(f'    - {k} tem o valor {v}')
