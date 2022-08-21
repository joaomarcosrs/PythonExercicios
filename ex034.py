salario = float(input('Digite o salário do(a) colaborador(a): '))

if salario > 1250:
    salario = salario * 1.10
    print('O novo salário do(a) colaborador(a) é: {:.2f}'.format(salario))
else:
    salario = salario * 1.15
    print('O novo salário do(a) colaborador(a) é: {:.2f}'.format(salario))
