nome = str(input('Digite seu nome: ')).strip()
nome = nome.split()
print('Seu primeiro no é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
