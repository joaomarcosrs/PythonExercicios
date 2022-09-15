print(f'{"-=-"*30}\n'
      f'{"Sequência de Fibonacci":^90}\n'
      f'{"-=-"*30}\n')

numero = int(input('Quantos termos de Fibonacci você deseja ver? '))

a = 0
b = 1
i = 3
lst_fibo = []
lst_fibo.append(str(a))
lst_fibo.append(str(b))

while i <= numero:
    soma = a + b
    lst_fibo.append(str(soma))
    a = b
    b = soma
    i = i + 1
print(f'\n{" ~ ".join(lst_fibo)}')    
print('\nFIM')