# import do método randint() para o palpite do computador
from random import randint

#O jogo consiste em um Par ou ímpar entre o computador e o usuário
print(f'{"-=-" * 20}\n'
      f'{"VAMOS JOGAR PAR OU ÍMPAR":^60}\n'
      f'{"-=-" * 20}\n')
#Atribui-se um contador para calcular quantas vezes será necessário até o usuário perder
i = 0
#inicío do laço de jogo
while True:
    #entrada do jogador
    jogador = int(input('Digite um número: '))

    #atribuição 'False' para a variável do palpite para a forçar a escolha do usuário entre P e I
    palpite = 'False'
    #inicío do laço para condicionar a escolha até o usuário escolher P ou I
    while palpite == 'False':
        #entrada do usuário entre P ou I, note que ignora-se os espaços, trabalha-se com maiúsculas e pega-se apenas a primeira letra
        palpite = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[:1]
        #Inicío da condição para tratamento de opções inválidas
        if palpite not in 'PI':
            print(f'\nOPÇÃO INVÁLIDA'
                  f'\nEscolha (P) para PAR ou (I) para ÍMPAR\n')
            palpite = 'False'
        else:
            #caso as opções corretas sejam digitadas, a execução sai do laço
            break
    #gera-se um número aleatótio entre 0 e 10 para o palpite do computador
    computador = randint(0, 10)
    #soma-se o número do jogador e do computador
    soma = computador + jogador
    #teste simples para saber se é Par ou Ímpar
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    #Mensagem ao usuário contendo os palpites, soma e resultado
    print(f'{"-" * 60}'
          f'\nVocê jogou {jogador} e o computador {computador}. Total de {soma} DEU {resultado}!\n'
          f'{"-" * 60}')
    #teste para saber se o usuário ou o computador venceu a partida
    #Caso o usuário vença, o jogo continua e o contador adiciona uma volta
    if soma % 2 == 0 and palpite in 'P' or soma % 2 != 0 and palpite in 'I':
        print(f'Você VENCEU!!!'
              f'\nVamos jogar novamente...\n')
        i = i + 1
    else:
        #Caso jogador perca o laço é interrompido
        print(f'Você PERDEU!!!')
        break
#pequena condição só para corrigir o plural
if i == 1:
    plu_sing = 'vez'
else:
    plu_sing = 'vezes'
#mensagem fina contado quantas partidas o usuário venceu
print(f'{"-=-" * 20}\n'
      f'GAME OVER! Você venceu {i} {plu_sing}.\n'
      f'{"-=-" * 20}\n')
