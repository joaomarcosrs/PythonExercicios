termo = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão da progressão: '))
pri_termo = termo

print(f'\n{"="*40}\n'
      f'{"Progressão Aritmética":^40}\n'
      f'{"="*40}\n')

print(f'O 1° termo é: {pri_termo:>3}\n'
      f'A razão é: {razao:>6}\n'
      f'Os 10 primeiros termos da PA são:\n')

print(pri_termo, end=' ')
i = 0
while i < 9:
  termo = termo + razao
  print(f'{termo}', end =' ')
  i = i + 1