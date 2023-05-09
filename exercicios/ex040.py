nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if  media < 5:
    print('Sua media foi: {} \033[31mEstá REPROVADO!!!\033[m'.format(media))
elif 5 <= media < 6.9:
    print('Sua media foi: {} \033[34mEstá RECUPERAÇÃO!!!\033[m'.format(media))
elif media >= 7:
    print('Sua media foi: {} \033[32mEstá APROVADO!!!\033[m'.format(media))
