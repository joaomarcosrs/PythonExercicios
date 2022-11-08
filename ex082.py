lst_numero = list()
lst_par = list()
lst_impar = list()
i = 0

while True:
  numero = int(input('Digite um número: '))

  while True:
    keep_loop = str(input('Você deseja continuar? [S/N] ')).strip().upper()[:1]

    if keep_loop not in 'SN':
      print('Reposta inválida! Digite [S] SIM ou [N] NÃO!')
    else:
      break
  if keep_loop in 'N':
    break

  lst_numero.append(numero)
  if lst_numero[i] % 2 == 0:
    lst_par.append(numero)
  else:
    lst_impar.append(numero)
  i += 1

print('-=-'*15)
print(f'A lista completa é: {lst_numero}')
print(f'A lista de pares é: {lst_par}')
print(f'Alista de ímpares é: {lst_impar}')
