numero = int(input('Digite um núemro inteiro: '))
resto = numero % 2

if resto == 0:
    print('O número digitado foi {} e ele é um número par!'.format(numero))
else:
    print('O número digitado foi {} e ele é um número ímpar!'.format(numero))
