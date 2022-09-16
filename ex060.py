###### FATORIAL USANDO WHILE #######
print(f'\n{"-=-"*6}Cálculo de Fatorial{"-=-"*6}\n')
numero = int(input('Digite um número: '))
lst_fatorial = []
fatorial = 1
i = numero

while numero > 0:
    fatorial = numero * fatorial
    lst_fatorial.append(str(numero))
    numero = numero - 1

print(f'\nO cálcullo de {i}! é...\n'
      f'\n{i}! = {" x ".join(lst_fatorial)} = {fatorial}')


# ###### FATORIAL USANDO FOR #######
# print(f'\n{"-=-"*6}Cálculo de Fatorial {"-=-"*6}\n')
# numero = int(input('Digite um número: '))

# lst_fatorial = []
# fatorial = 1
# for i in range(numero, 0, -1):
#   fatorial = i * fatorial
#   lst_fatorial.append(str(i))

# print(f'\nO cálcullo de {numero}! é...\n'
#       f'\n{numero}! = {" x ".join(lst_fatorial)} = {fatorial}')


# Existe um módulo math com o método factorial()

