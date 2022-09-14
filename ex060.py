print(f'\n{"-=-"*6}Cálculo do Fatorial{"-=-"*6}')
numero = int(input('Digite um número: '))
# i = numero
fatorial = 1
while numero > 0:
    fatorial = numero * fatorial
    numero = numero - 1
print(fatorial)


