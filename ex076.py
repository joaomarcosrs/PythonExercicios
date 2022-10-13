tpl_produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)

print(f'{"-" * 41}\n'
      f'{"LISTAGEM DE PREÇOS":^41}\n'
      f'{"-" * 41}\n')

c = 1
for i in range(0, len(tpl_produtos), 2):
    print(f'{tpl_produtos[i]:.<32}R$ {tpl_produtos[c]:>6.2f}')
    c = c + 2

print(f'\n{"-"*41}')
