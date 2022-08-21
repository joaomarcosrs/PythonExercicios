#print('\033[7;34mOlá, mundo!\033[m')


# a = 3
# b = 5
# print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))

nome = 'João'
#Pode-se criar um dicionário de cores pra ajudar e substituir nas variáveis
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!'.format(cores['azul'], nome, cores['limpa']))
#print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[1;30;44m', nome, '\033[m'))
