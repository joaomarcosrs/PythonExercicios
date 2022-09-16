from random import randint
from time import sleep

num_random = randint(0, 10)
print(f'{"-=-"*20}'
      f'\nVou escolher um número entre 0 e 10, tente acertar....'
      f'\n{"-=-"*20}')
sleep(2)
num_digit = -1
i = 0
while num_random != num_digit:
    num_digit = int(input('Eu já escolhi o meu, agora é sua vez: '))
    print('CARREGANDO...\n')
    sleep(3)
    i = i + 1
    if num_random == num_digit:
        print(f'Você ACERTOU, eu também escolhi {num_random}')
    elif num_random > num_digit:
        print(f'Mais... Tente novamente')
    else:
        print(f'Menos... Tente novamente')
print(f'Você precisou de {i} tentativa(s)')
