veloc = int(input('Digite a velocidade do carro: '))


multa = veloc - 80
if multa <= 0:
    print('Você está dentro do limite de velocidade!')
else:
    print('Você ultrapassou o limite de volocidade em {} Km/h irá pagar R${:.2f} em multa'.format(multa, multa * 7))
