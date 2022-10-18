# num = (2, 5, 9)
# # num[2] = 3 #Isso não vai ser possível assim, pois a Tupla é imutável
# print(num)
#
# #############################################################################################
# num = [2, 5, 9]
# num[2] = 3 #Como a Lista é mutável, dessa forma é possível fazer as alterações na lista
# print(num)
#
# # Porém eu não consigo utilizar o mesmo comando para adicionar novos elementos, algo como:
# # num[3] = 4
# # Para isso, é necessário utilizar o método append()
# num.append(7)
# print(num)
#
# #############################################################################################
# num = [8, 3, 2, 5, 9]
# num.append(7)
# print(num)
#
# num.sort()
# print(num)
#
# num.sort(reverse=True)
# print(num)
#
# #################################################################################################
# num = [8, 3, 2, 5, 9]
# num.append(7)
# print(num)
# print(sorted(num))
# num.insert(2, 0)
# print(num)
#
# ################################################################################################
# num = [8, 3, 2, 5, 9]
# num.append(7)
# print(num)
# print(sorted(num))
# num.insert(2, 0)
# print(num)
# num.pop()
# print(num)
# num.pop(2)
# print(num)
#
# ##################################################################################################
# valores = [] #outra forma de atribuir uma lista vazia é valores = list()
# valores.append(5)
# valores.append(9)
# valores.append(4)
#
# # for v in valores:
# #     print(f'{v}...', end='')
#
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}!')
# print('Cheguei ao final da lista')
#
# ##################################################################################################
# valores = list()
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))
#
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}!')
# print('Cheguei ao final da lista')

###################################################################################################
print('\n')
a = [2, 3, 4, 7]
#### b = a      # Somete assim cria-se uma ligação entre as listas e todas as alterações serão feitas nas duas listas
#Para criar uma cópia basta fazer:
b = a[:] #Aqui atribui-se todos os elemento da lista A à lista B
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
# A partir do momento que atribui-se uma lista à outra, o python cria uma ligação entre elas.
