# cont = 0                                          #Contador
# lista = []                                        #A lista que irá recerber os 'dados'
# pos = 0                                           # IPORTANTE Será usado como referencia no código
# while True:
#      dados = []                                   #Toda repetição será limpa pra que seja adicionada novos elementos
#      nome = str(input('Nome: '))                  #Recebe o nome
#      dados.append(nome)                           #Adiciona um novo elemento(nome) em 'dados'
#      peso = float(input('Peso: '))                #Recebe o peso
#      dados.append(peso)                           #Adiciona um novo elemento(peso) em 'dados'
#      if cont == 0 or peso > dados[-1]:            #Se o contador for 0 ou peso maior do que já esta adicionado no último elemento
#           lista.append(dados[:])                  #Adicione todos os elementos de 'dados' na última posição na 'lista'
#      else:
#           while pos < len(lista[:]):              #Enquanto 'pos' for menor que quantidade de ELEMENTOS em 'lista'
#                if peso <= lista[pos][1]:          #Se 'peso' for menor ou igual que o elemento na posição [pos][1]
#                     lista.insert(pos, dados[:])   #Adiciona todos os elementos de 'dados' em 'lista' e interrompe a repetição
#                     break
#                pos += 1                           #Incrementa mais um a 'pos' a cada repetição,
#                                                   # fazendo o 'if' mudar de elemento na 'lista' com o [pos]
#      resp= ' '
#      while resp not in 'SsNn':                    #Enquanto 'r' não estiver dentro de 'SsNn'
#           resp = str(input('Quer continuar? [S/N] ')).strip()[0] #'resp' receber um resposta,
#                                                                  # retira espaços laterais e pega somente a primeira letra
#      if resp in 'Nn':                             #Se a resposta recebida entiver dentro de 'Nn' interrompa a repetição
#           break
#      cont = 1
# print(lista)
#
# print(f'O maior peso foi de {lista[pos][1]}')

'''GUANABARA'''
'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. 
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

# temp = []
# princ = []
# mai = men = 0
# while True:
#      temp.append(str(input('Nome: ')))       #recebe nome
#      temp.append(float(input('Peso: ')))     #recebe peso
#      if len(princ) == 0:                     #na primeira execução
#           mai = men = temp[1]                #maior e o menor recebe o temp[1] cadastrado
#      else:
#           if temp[1] > mai:                  #se o segundo elemento de 'temp' for maior que 'mai'
#                mai = temp[1]                 #mai recebe o segundo elemento
#           if temp[1] < men:                  #se o segundo elemeno cadastrado for menor que o 'men'
#                men = temp[1]                 #'men' recebe o segundo elemento
#      princ.append(temp[:])                   #pega a copia
#      temp.clear()                            #limpa a lista
#      resp = str(input(('Quer continuar: [S/N] ')))
#      if resp in 'Nn':
#           break
# print('-='*30)
# print(f'Os dados foram {princ}')
# print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
# print(f'O maior peso foi de {mai}Kg. Peso de', end='')
# for p in princ:
#      if p[1] == mai:
#           print(f'[{p[0]}]', end='')
# print(f'O menor peso foi de {men}Kg. Peso de ', end='')
# for p in princ:
#      if p[1] == men:
#           print(f'[{p[1]}]', end='')


temp = []      #lista temporaria
princ = []     #lista principal
mai = men = 0  #maio e menor igual a 0
while True:
     temp.append(str(input('Nome: ')))       #recebe o nome
     temp.append(float(input('Peso: ')))     #recebe o peso
     if len(princ) == 0:                     #se o tamanho de principal for igual a 0 então
          mai = men = temp[1]                #maio e menor recebe o segundo elemento de temp
     else:
          if temp[1] > mai:        #se o segundo elemento de temp for maior que mai então
               mai = temp[1]       #mai recebe o segundo elemento de temp
          if temp[1] < men:        #se o segundo elemento de temp for menor que men então
               men = temp[1]       #men recebe o segundo elemento de temp
     princ.append(temp[:])         #princ recebe um copia do temp
     temp.clear()                  #temp é limpo pra proxima repetição do loop
     resp = str(input('Quer continuar? [S/N] '))            #pergunta se quer continuar
     if resp in 'Nn':                                       #se nao quebre o loop
          break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')     #imprime o total de pessoas cadastradas
print(f'O maior peso foi de {mai}Kg. peso de ', end='')     #imprimi o maior peso junto com o nome da pessoas
for p in princ:
     if p[1] == mai:                         #se o segundo valor de princ for igual a mai então
          print(f'[{p[0]}]', end='')         #imprime o nome da(s) pessoa(s)
print()
print(f'O maior peso foi de {men}Kg. Peso de ', end='')     #imprime o menor peso junco com os nome das pessoas
for p in princ:
     if p[1] == men:                         #se o segundo valor de princ for igual a men então
          print(f'[{p[0]}]', end='')         #imprime o primeiro elemento de princ
print()
