from time import sleep

def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analizando ps valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram infomados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
    print()

#Prgrama principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 5, 0)
maior(1, 2)
maior()
