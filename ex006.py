numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = pow(numero, (1/2))
print('O número digitado foi: {}'
      '\nO dobro é: {}'
      '\nO triplo é: {}'
      '\nA raiz quadrada é: {:.3f}'
      .format(numero, dobro, triplo, raiz))
