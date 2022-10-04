tpl_produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)

print(f'{"-" * 50}\n'
      f'{"LISTAGEM DE PREÇOS":^50}\n'
      f'{"-" * 50}')

c = 1
for i in range(0, len(tpl_produtos), 2):
    print(f'{tpl_produtos[i]:<1}{"."*30:>}{tpl_produtos[c]:>6.2f}')
    c = c + 2