num = int(input('Digite um Número: '))

print('Escolha uma das bases para conversão:\n'
      '\033[1;34m1\033[m_ Para binário\n'
      '\033[1;34m2\033[m_ Para octal\n'
      '\033[1;34m3\033[m_ Para hexadecimal')

opcao = int(input('Base númerica que gostaria de converter: '))

if opcao == 1:
    result = bin(num)[2:]
    print('O número {} em binário é: {}'.format(num, result))
elif opcao == 2:
    result = oct(num)[2:]
    print('O número {} em Octal é: {}'.format(num, result))
elif opcao == 3:
    result = hex(num)[2:]
    print('O número {} em Hexadecimal é:{}'.format(num, result))
else:
    print('\033[1;31mEscolha incorreta!!!\033[m')