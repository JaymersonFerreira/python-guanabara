# expressão = str(input('Digite um expressão: '))
# abre = expressão.count('(')
# fecha = expressão.count(')')
# if  abre == fecha:
#     print('\033[032Sua expreção esta correta.\033[m')
# else:
#     print('\033[31mSua expressão esta errada\033[m')

'''GUANABARA'''
'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

# expr = input('Digite a expressão: ')
# pilha = []
# for simb in expr:
#     if simb == '(':
#         pilha.append('(')
#     elif simb == ')':
#         if len((pilha) > 0):
#             pilha.pop()
#         else:
#             pilha.append(')')
#             break
# if len(pilha) == 0:
#     print('Sua expressão está válida')
# else:
#     print('Sua expresssão está invalida')

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
