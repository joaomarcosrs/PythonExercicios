from time import sleep

algo = input('\033[1m Digite algo: \033[m')

print('\n|\033[1;35;40m{:18}{}{:18}\033[m|'.format('='*18,'ANALISANDO','='*18))
print('|{}|'.format(' ' * 46))
sleep(2)

#Identificação do tipo primititvo
print('| O tipo primitivo desse valor é \033[1;34m{}\033[m |'.format(type(algo)))
#Teste para saber se possui só espaços ou não
if algo.isspace():
    print('| Só tem espaços? \033[1;32m{:>28}\033[m |'.format('True'))
else:
    print('| Só tem espaços? \033[1;31m{:>28}\033[m |'.format('False'))

#Teste para saber se o valor digitado é um número
if algo.isnumeric():
    print('| É um número? \033[1;32m{:>31}\033[m |'.format('True'))
else:
    print('| É um número? \033[1;31m{:>31}\033[m |'.format('False'))

#Teste se o valor digitado é alfabético
if algo.isalpha():
    print('| É alfabético? \033[1;32m{:>30}\033[m |'.format('True'))
else:
    print('| É alfabético? \033[1;31m{:>30}\033[m |'.format('False'))

#Teste se o valor digitado é alfanumérico
if algo.isalnum():
    print('| É alfanumérico? \033[1;32m{:>28}\033[m |'.format('True'))
else:
    print('| É alfanumérico? \033[1;31m{:>28}\033[m |'.format('False'))

#Teste se o valor digitado é maiúscula
if algo.isupper():
    print('| Está em maiúsculas? \033[1;32m{:>24}\033[m |'.format('True'))
else:
    print('| Está em maiúsculas? \033[1;31m{:>24}\033[m |'.format('False'))

#Teste se o valor digitado é minúsucula
if algo.islower():
    print('| Está em minúsculas? \033[1;32m{:>24}\033[m |'.format('True'))
else:
    print('| Está em minúsuclas? \033[1;31m{:>24}\033[m |'.format('False'))

#Teste se o valor digitado está capitalizado
if algo.istitle():
    print('| Está capitalizada? \033[1;32m{:>25}\033[m |'.format('True'))
else:
    print('| Está capitalizada? \033[1;31m{:>25}\033[m |'.format('False'))

print('|{}|'.format('_' * 46))