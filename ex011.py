largura = float(input('Digite a largura em metros: '))
altura = float(input('Digite a altura em metros: '))

area = largura * altura
pintar = area / 2

print('A área da parede é {}m² e você vai precisar de {} litros de tinta'.format(area, pintar))