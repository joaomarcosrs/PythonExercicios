from math import cos, sin, tan, radians

angulo = float(input('Digite a medida do ângulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O ângulo é: {}º'
      '\nO seno é: {:.2f}'
      '\nO cosseno é: {:.2f}'
      '\nA tangente é: {:.2f}'
      .format(angulo, seno, cosseno, tangente))
