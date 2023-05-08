# continuar = 'S'
# idade = sexoM = mulher20 = maiorIdade = 0
# while True:
#     if continuar == 'N':
#         break
#     if continuar == 'S':
#         print('=' * 30)
#         print('CADASTRE UM PESSOA')
#         print('-' * 30)
#         idade = int(input('Idade: '))
#         while True:
#             sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
#             if sexo =='M' or sexo == 'F':
#                 break
#         if idade >= 18:
#             maiorIdade += 1
#         if sexo == 'M':
#             sexoM += 1
#         if sexo == 'F' and idade < 20:
#             mulher20 += 1
#         while True:
#             continuar = str(input('Quer continuar: [S/N] ')).upper().strip()[0]
#             if continuar == 'S' or continuar == 'N':
#                 break
#         print('=' * 30)
#
# print(f'Total de pessoas com mais de 18 anos: {maiorIdade}')
# print(f'Ao todo temos {sexoM} homens cadastrados')
# print(f'E temos {mulher20} com menos de 20 anos')


'''GUANABARA'''

# tot18 = totH = totM20 = 0
# while True:
#     idade = int(input('Idade:'))
#
#     sexo = ' '
#     while sexo not in 'MF':
#         sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
#
#     if idade >= 18:
#         tot18 += 1
#     if sexo == 'M':
#         totH += 1
#     if sexo == 'F' and idade < 20:
#         totM20 += 1
#
#     resp = ' '
#     while resp not in 'SN':
#         resp = str(input('Quer continuar: ')).strip().upper()[0]
#     if resp == 'N':
#         break
# print(f'Total de pessoas com mais de 18 anos: {tot18}')
# print(f'Ao todo temos {totH} homens cadastrados')
# print(f'E temos {totM20} mulheres com menos de 20 anos')


'''eu'''
maior18 = mulher20 = homens = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper().strip()[0]

    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {homens} homem cadastrados')
print(f'E temos {mulher20} com menos de 20 anos')