from random import randint

def jokenpo():
  print('\n\nVamos jogar Jokenpô?')
  opcao_msg = '''
Escolha uma opção:

[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
[ 0 ] TERMINAR O JOGO

Já escolhi o meu!!!
'''
  opcao = int(input(opcao_msg))
  def cond_inicial():
    global cond_escolha
    cond_escolha = opcao == 1 or opcao == 2 or opcao == 3

  def cond_game():
    global cond_empate
    global cond_vitoria
    global cond_derrota
    cond_empate = escolha_pc == 'Pedra' and opcao == 1 or escolha_pc == 'Papel' and opcao == 2 or escolha_pc == 'Tesoura' and opcao == 3
    cond_vitoria = escolha_pc == 'Pedra' and opcao == 3 or escolha_pc == 'Papel' and opcao == 1 or escolha_pc == 'Tesoura' and opcao == 2
    cond_derrota = escolha_pc == 'Pedra' and opcao == 2 or escolha_pc == 'Papel' and opcao == 3 or escolha_pc == 'Tesoura' and opcao == 1

  if opcao == 0:
    print('\nMuito Obrigado por jogar comigo. Até a próxima!')
  elif cond_escolha:
      jo_list = ['Pedra', 'Papel', 'Tesoura']
      i = randint(0, 2)
      escolha_pc = jo_list[i]
      cond_game()

      if cond_empate:
        print('\nEMPATAMOS! Eu também escolhi {}'.format(escolha_pc))
        print('Vamos de novo!')
        jokenpo()
      elif cond_vitoria:
        print('\nVenci!!! Eu escolhi {}'.format(escolha_pc))
        print('Você quer jogar de novo?')
        jokenpo()
      elif cond_derrota:
        print('\nPerdi!!! Eu escolhi {}'.format(escolha_pc))
        print('Me dê outra chance...')
        jokenpo()

jokenpo()