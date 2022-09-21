# import do método randint() para o palpite do computador
from random import randint

#O jogo consiste em um Par ou ímpar entre o computador e o usuário
print(f'{"-=-" * 20}\n'
      f'{"VAMOS JOGAR PAR OU ÍMPAR":^60}\n'
      f'{"-=-" * 20}\n')
#Esse contador é
i = 0
while True:
    jogador = int(input('Digite um número: '))

    palpite = 'False'
    while palpite == 'False':
        palpite = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[:1]
        if palpite not in 'PI':
            print(f'\nOPÇÃO INVÁLIDA'
                  f'\nEscolha (P) para PAR ou (I) para ÍMPAR\n')
            palpite = 'False'
        else:
            break

    computador = randint(0, 10)
    soma = computador + jogador

    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'

    print(f'{"-" * 60}'
          f'\nVocê jogou {jogador} e o computador {computador}. Total de {soma} DEU {resultado}!\n'
          f'{"-" * 60}')

    if soma % 2 == 0 and palpite in 'P' or soma % 2 != 0 and palpite in 'I':
        print(f'Você VENCEU!!!'
              f'\nVamos jogar novamente...\n')
        i = i + 1
    else:
        print(f'Você PERDEU!!!')
        break

    if i == 1:
        plu_sing = 'vez'
    else:
        plu_sing = 'vezes'

print(f'{"-=-" * 20}\n'
      f'GAME OVER! Você venceu {i} {plu_sing}.\n'
      f'{"-=-" * 20}\n')
