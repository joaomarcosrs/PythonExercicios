dist = float(input('Digite a distância da viagem em Km: '))

if dist <= 200:
    dist = dist * 0.50
else:
    dist = dist * 0.45
print('O preço da passagem é R${:.2f}'.format(dist))
