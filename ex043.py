altura = str(input('Digite a altura do indivíduo em metros: ')).replace(',','.')
altura = float(altura)
peso = str(input('Digite o peso do indivíduo em kilos: ')).replace(',','.')
peso = float(peso)

imc = round(peso / (altura**2), 1)
print('\n')
if imc < 18.5:
  print('O indivíduo tem um IMC de {} e está Abaixo do Peso!'.format(imc))
elif imc >= 18.5 and imc < 25:
  print('O indivíduo tem um IMC de {} e está com um Peso Ideal!'.format(imc))
elif imc >= 25 and imc < 30:
  print('O indivíduo tem um IMC de {} e está com Sobrepeso!'.format(imc))
elif imc >= 30 and imc < 40:
  print('O indivíduo tem um IMC de {} e esta com Obesidade!'.format(imc))
elif imc >= 40:
  print('O indivíduo tem um imc de {} e está com Obesidade Mórbida!'.format(imc))