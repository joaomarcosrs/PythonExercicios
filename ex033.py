number_list = []
print('Vamos verm que é maior ou menor...')

for i in range(3):
    number = float(input('Digite um número número: '))
    number_list.append(number)

number_odered = sorted(number_list)
print('O número menor é {} e o número maior é {}'.format(number_odered[0], number_odered[2]))

############################ Solução Professor #############################

# num1 = int(input('Digite o primeiro valor: '))
# num2 = int(input('Digite o segundo valor: '))
# num3 = int(input('Digite o terceiro valor: '))
#
# #Verificando quem é o menor
# menor = num1
# if num2 < num1 and num2 < num3:
#     menor = num2
# if num3 < num1 and num3 < num2:
#     menor = num3
# #Verificando quem é o maior
# maior = a
# if num2 > num1 and num2 > num3:
#     maior = num2
# if num3 > num1 and num3 > num2:
#     maior = num3
# print('O menor valor digitado foi {}'.format(menor))
# print('O maior valor digitado foi {}'.format(maior))

