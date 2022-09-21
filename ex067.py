while True:
    numero = int(input('\nDeseja ver a tabuada de que valor? '))
    if numero < 0:
        print('PROGRAMA ENCERRADO! Volte Sempre!')
        break

    ### SOMA ###
    print(f'\n{"~" * 3} SOMA {"~" * 3}')
    for i in range(0, 11):
        print(f'{i:>2} + {numero} = {i + numero:>2}')

    ### SUBTRAÇÃO ###
    print(f'\n{"~" * 3} SUBTRAÇÃO {"~" * 3}')
    for i in range(0, 11):
        print(f'{i:>2} - {numero} = {i - numero:>2}')

    ### MULTIPLICAÇÃO ###
    print(f'\n{"~" * 3} MULTIPLICAÇÃO {"~" * 3}')
    for i in range(0, 11):
        print(f'{i:>2} * {numero} = {i * numero:>2}')

    ### Divisão ###
    print(f'\n{"~" * 3} DIVISÃO {"~" * 3}')
    for i in range(0, 11):
        print(f'{i:>2} / {numero} = {i / numero:>2}')