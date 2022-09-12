termo = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão da progressão: '))
pri_termo = termo
print(
    f'\n{"="*40}\n'
    f'{"Progressão Aritmética":^40}\n'
    f'{"="*40}\n')

print(f'O 1° termo é: {pri_termo:>3}')
print(f'A razão é: {razao:>6}\n')
print(f'Os 10 primeiros termos da PA são:\n')

print(pri_termo, end=' ')
for i in range(0, 9):
  termo = termo + razao
  print(f'{termo}', end =' ')



# # Solução do Professor #
# primeiro = int(input('Primeiro termo: '))
# razao = int(input('Razão: '))
# decimo =  primeiro + (10 - 1) * razao
# for c in range(primeiro, decimo + razao, razao):
#   print(f'{c}', end=' → ')
# print('ACABOU')