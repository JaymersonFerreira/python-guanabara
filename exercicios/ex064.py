num = cont = soma = 0
num = int(input('Digite um número para soma: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número para soma: '))
print('Foram inseridos {}'.format(cont))
print('A soma é: {}'.format(soma))
