from random import randint

tpl_int = ()
for i in range(0, 5):
   item = (randint(0, 11), )
   tpl_int = tpl_int + item
print(f' Os número sorteados foram: ', end='')
for c in tpl_int:
  print(f'{c}', end=' ')
print(f'\nO maior número sorteado foi: {max(tpl_int)}'
      f'\nO menor número sorteado foi: {min(tpl_int)}')
