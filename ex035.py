line_one = float(input('Digite o valor da primeira reta: '))
line_two = float(input('Digite o valor da segunda reta: '))
line_three = float(input('Digite o valor da terceira reta: '))

cond_a = abs(line_two - line_three) < line_one < line_two + line_three
cond_b = abs(line_one - line_three) < line_two < line_one + line_three
cond_c = abs(line_one - line_two) < line_three < line_one + line_two

if cond_a and cond_b and cond_c:
    print('As retas {}, {} e {} podem formar um triângulo'.format(line_one, line_two, line_three))
else:
    print('As retas {}, {} e {} não podem formar um triângulo'.format(line_one, line_two, line_three))

