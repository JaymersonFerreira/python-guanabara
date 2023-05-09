# a = 4
# b = 5
# s = a + b
# print(s)
# a = 8
# b = 9
# s = a + b
# print(s)
# a = 2
# b = 1
# s = a + b
# print(s)

# def soma(a, b):
#     s = a + b
#     print(s)
#
# #programa principal
# soma(4 , 5)
#
# soma(8, 9)
#
# soma(2, 1)


# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma A + B = {s}')

#Programa peincipal
# soma(4, 5)
# soma(b=4, a=5)
# '''A = 5 e B = 4
# A soma A + B = 9'''


# def soma(* valores): #desempacotamento
#     s = 0
#     for num in valores:
#         s += num
#     print(f'Somando os valores {valores}  temos {s}')
# soma (5, 2)
# soma(2, 9, 4)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
