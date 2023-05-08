import random
from time import sleep
pedra = 1
tesoura = 2
papel = 3

pc = random.randint(1, 3)
print('Escola:\n'
      '[ 1 ] Pedra\n'
      '[ 2 ] Papel\n'
      '[ 3 ] Tesoura')
vc = int(input('Qual a sua jogada: '))
sleep(0.2)
print('JO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PO!!!')
sleep(0.3)
if vc == 1 and pc == 1 or vc == 2 and pc == 2 or vc == 3 and pc == 3:
    print('\033[35mEmpate!!!\033[m')
elif vc == 1 and pc == 2:
    print('vc escolheu: \033[36mPedra\033[m, pc escolheu: \033[36mPapel\033[m. \033[31mVc perdeu!!!\033[m')
elif vc == 1 and pc == 3:
    print('vc escolheu: \033[36mPedra\033[m, pc escolheu: \033[36mTesoura\033[m. \033[32mVc ganhou!!!\033[m')
elif vc == 2 and pc == 1:
    print('vc escolheu: \033[36mTesoura\033[m, pc escolheu: \033[36mPedra\033[m. \033[32mVc ganhou!!!\033[m')
elif vc == 2 and pc == 3:
    print('vc escolheu: \033[36mTesoura\033[m, pc escolheu: \033[36mPapel\033[m. \033[31mVc perdeu!!!\033[m')
elif vc == 3 and pc == 1:
    print('vc escolheu: \033[36mPapel\033[m, pc escolheu: \033[36mPedra\033[m. \033[31mVc perdeu!!!\033[m')
elif vc == 3 and pc == 2:
    print('vc escolheu: \033[36mPapel\033[m, pc escolheu: \033[36mTesoura\033[m. \033[32mVc venceu!!!\033[m')
else:
    print('\033[33mEscolha incorreta!!!\033[m')
