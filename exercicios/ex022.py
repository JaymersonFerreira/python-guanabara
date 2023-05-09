print('--' * 20)
nome = str(input('Nome completo: '))
print('--' * 20)

nome = nome.strip()

nomeM = nome.upper()
nomeM = ' '.join(nomeM.split())

nomeN = nome.lower()
nomeN = ' '.join(nomeN.split())

nomeCou = len(''.join(nome.split()))

divido = nome.strip().split()
quaPriNome = len(divido[0])

print('Nome Maiúsculas: {}'.format(nomeM))
print('Nome Minúsculas : {}'.format(nomeN))
print('Quantidade de letras sem espaços: {}'.format(nomeCou))
print('Quantidade de letras do primeiro nome: {}'.format(quaPriNome))
print('--' * 20)


nome = str(input('Digite seu nome completo: ')).strip()
print('Analizando seu nome...')
print('Seu nome em maiúscula é {}'.format(nome.upper()))
print('Seu nome em minúscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))