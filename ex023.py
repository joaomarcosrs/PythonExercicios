### Como string ####
'''numero = str(input('Digite um número: '))

print('unidade: {}'
      '\ndezenda: {}'
      '\ncentena: {}'
      '\nmilhar: {}'.format(numero[3], numero[2], numero[1], numero[0]))
'''

### Como inteiro ####
numero2 = int(input('Digite um número: '))

uni = numero2 // 1 % 10
dez = numero2 // 10 % 10
cen = numero2 // 100 % 10
mil = numero2 // 1000 % 10

print('unidade: {}'
      '\ndezena: {}'
      '\ncentena: {}'
      '\nmilhar: {}'.format(uni, dez, cen, mil))

