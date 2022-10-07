tpl_num = (
'zero', 'um', 'dois', 'três', 'qautro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('\nDigite um número inteiro entre 0 e 20: '))
    if numero not in range(0, 21):
        print('\nOpção Inválida!')
    else:
        print(f'\nO número digitado foi {tpl_num[numero]}\n')

        while True:
            keep_loop = str(input('Você deseja continuar[S/N]? ')).strip().upper()[:1]
            if keep_loop not in 'SN':
                print(f'Digite [S] para SIM e [N] para NÃO.')
            else:
                break
        if keep_loop == 'N':
            print('Você decidiu não continuar... Até a próxima!')
            break