preco = str(input('Digite o preço do produto: ')).replace(',', '.')
preco = float(preco)

opcao = int(input('''
Escolha a opção de pagamento...
[ 1 ] À vista - dinheiro/cheque
[ 2 ] À vista - cartão
[ 3 ] Até 2x  - cartão
[ 4 ] À partir de 3x - cartão\n\n'''))

if opcao == 1:
  preco = round(preco * 0.9, 2)
  print('Você escolheu a opção: À vista (dinheiro ou cheque). Parabéns, ganhou 10% de desconto!')
  print('Você irá pagar R$ {:.2f}'.format(preco))
elif opcao == 2:
  preco = round(preco * 0.95, 2)
  print('Você escolheu a opção: À vista (cartão). Parabéns, ganhou 5% de desconto!')
  print('Você irá pagar R$ {:.2f}'.format(preco))
elif opcao == 3:
  parcela = preco / 2
  print('Você escolheu a opção: Até 2 vezes (cartão)!')
  print('Você irá pagar R$ {:.2f}'.format(preco))
  print('Cada parcela ficará no valor de R$ {}'.format(parcela))
else:
  n = int(input('Digite o número de parcelas: '))
  preco = preco * 1.20
  parcela = preco / n
  print('Você escolheu a opção: À partir de 3 vezes (cartão). Será feito um acréscimo de 20% de juros!')
  print('Você irá pagar no total R$ {:.2f}. \nDividido em {} parcelas, cada uma no valor de R$ {:.2f}.'.format(preco, n, parcela))