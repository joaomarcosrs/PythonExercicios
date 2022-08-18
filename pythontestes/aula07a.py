num1 = int(input('Um valor: '))
num2 = int(input('Outro valor: '))
soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
divint = num1 // num2
exp = num1 ** num2
print('A soma vale {}, a subtração vale {}, a multiplicação vale {} e a divisão vale {:.3f}'
      .format(soma, sub, mult, div))
print('A divisão inteira vale {} e a exponeciação vale {}'.format(divint, exp))