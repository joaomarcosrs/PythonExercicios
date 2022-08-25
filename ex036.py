
#Entrada do valor da casa
v_casa = float(input('Digite o valor da casa que o cliente quer comprar: '))

#Entrada do valor do salário do cliente
v_salario = float(input('Digite o valor do salário do cliente: '))

#Entrada de um inteiro indicando a quantidade de anos em que a casa será quitada
anos = int(input('Digite em quantos anos o cliente pretende pagar a casa: '))

#Armazenamento dos meses em uma variável, pois será necesseráio o cálculo da prestação mensal
meses = anos * 12
#Calculo do valor da parcela
parcela = v_casa / meses
#Condição de compra da casa
cond_compra = v_salario * 0.30


#A condição para empréstimo é que cada parcela exceda o salário em até 30%
if parcela <= cond_compra:
    print('\nA quantidade de parcelas são (meses): {:>7}'
          '\nO valor de cada parcela é (R$): {:>9}{:.2f}'
          '\nO limite de cada parcela é (R$): {:>7}{:.2f}'
          '\n\n\033[1;32;40mO empréstimo foi autorizado!\033[m'.format(meses, '', parcela, '', cond_compra))
else:
    print('\nA quantidade de parcelas são (meses): {:>7}'
          '\nO valor de cada parcela é (R$): {:>9}{:.2f}'
          '\nO limite de cada parcela é (R$): {:>7}{:.2f}'
          '\n\n\033[1;31;40mO empréstimo não foi autorizado!\033[m'.format(meses, '', parcela, '', cond_compra))

