from time import sleep

opcao = 4
while opcao != 5:
    if opcao == 4:
        num_pri = str(input('Digite o primeiro valor: ')).strip().replace(',', '.')
        num_seg = str(input('Digite o segundo valor: ')).strip().replace(',', '.')
        num_pri = float(num_pri)
        num_seg = float(num_seg)

    sleep(1.5)
    opcao = int(input(f'\nESCOLHA UMA OPÇÃO'
                      f'\n[1] SOMAR'
                      f'\n[2] MULTIPLICAR'
                      f'\n[3] MAIOR'
                      f'\n[4] NOVOS NÚMEROS'
                      f'\n[5] SAIR\n'))
    if opcao == 1:
        print(f'\nVocê escolheu a {opcao}ª opção.\n'
              f'A soma é: {num_pri} + {num_seg} = {num_pri + num_seg}')
    elif opcao == 2:
        print(f'\nVocê escolheu a {opcao}ª opção.\n'
              f'A multiplicação é: {num_pri} * {num_seg} = {num_pri * num_seg}')
    elif opcao == 3:
        if num_pri >= num_seg:
            maior = num_pri
        else:
            maior = num_seg
        print(f'\nVocê escolheu a {opcao}ª opção.\n'
              f'O maior número entre {num_pri} e {num_seg} é {maior}.')
    elif opcao == 4:
        print(f'\nOk! Escolha novos números!')
    elif opcao == 5:
        print(f'\nVocê saiu do programa. Até logo!')
        print('FIM')
    else:
        print('\nVocê digitou uma opção inválida. Tente novamente!')
