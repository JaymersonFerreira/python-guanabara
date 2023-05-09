'''GUANABARA'''
'''Exercício Python 090: Faça um programa que leia nome e média de um aluno, 
guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''
# #Dividido em 3 partes:
# #1ª_Revebe o nome e a média e atribuir no dicionário
# aluno = dict()
# aluno['nome'] = str(input('Nome: '))
# aluno['Media'] = float(input(f'Media de {aluno["nome"]} '))
# #2ª_A verificação da média
# if aluno['Media'] >= 7:
#     aluno['situação'] = 'Aprovado'
# elif 5 <= aluno['Media'] < 7:
#     aluno['situação'] = 'Recuperação'
# else:
#     aluno['situação'] = 'Reprovado'
# #3ª_Impressão dos dados
# print('-=' * 20)
# for k, v in aluno.items():  #Para cada Chave um Valor   #itens() conjunto de chave e valor
#     print(f'  - {k} é igual a {v}')


aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'O {k} é igual a {v}')