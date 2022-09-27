lst_produto = []
lst_preco = []
lst_preco_mil = []

print(f'\n{"-=-" * 15}\n'
      f'{"LOJA FICTÍCIA":^45}\n'
      f'{"-=-" * 15}')
while True:
  produto = str(input('\nNome do produto: ')).strip().capitalize()
  preco =  str(input('Preço(R$): ')).replace(',', '.')
  lst_produto.append(produto)
  lst_preco.append(float(preco))

  while True:
    keep_loop = str(input('Você deseja continuar [S/N]? ')).strip().upper()[:1]
    if keep_loop not in 'SN':
      print(f'\nOpção Inválida!!!\n'
            f'Digite [S] para SIM e [N] para NÃO.\n')
    if keep_loop in 'SN':
      break
  if keep_loop in 'N':
    for i in range(len(lst_produto)):
      if lst_preco[i] > 1000:
        lst_preco_mil.append(lst_preco[i])
    break
indice = lst_preco.index(min(lst_preco))

print(f'\n{"=" * 15}FIM DO PROGRAMA{"=" * 15}\n\n'
      f'O total da compra foi R${sum(lst_preco):.2f}\n'
      f'Temos {len(lst_preco_mil)} produtos custando mais de R$1000.00\n'
      f'O produto mais barato foi {lst_produto[indice]} que custa R${min(lst_preco):.2f}')