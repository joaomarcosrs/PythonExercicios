from random import randint
from time import sleep
num_random = randint(0, 5)

print('-=-' * 20,
      '\nVou escolher um número entre 0 e 5, tente acertar... \n',
      '-=-' * 20)
sleep(2)
num_digit = int(input('Eu já escolhi o meu, agora é sua vez: '))
print('CARREGANDO...')
sleep(3)

if num_digit == num_random:
    print('Eu escolhi o número {}'.format(num_random))
    print('Você acertou o número, você venceu!')
else:
    print('Eu escolhi o número {}'.format(num_random))
    print('Você errou o número, você perdeu!')