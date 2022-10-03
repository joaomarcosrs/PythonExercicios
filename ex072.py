tpl_num = ('zero', 'um', 'dois', 'três', 'qautro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
  numero = int(input('Digite um número inteiro entre 0 e 20: '))
  if numero not in range(0, 21):
    print('Opção Inválida!')
  else:
    print(f'\nO número digitado foi {tpl_num[numero]}')
    break
