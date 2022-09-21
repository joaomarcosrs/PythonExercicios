soma = i = 0
while True:
    numero = int(input('Digite um número (ou digite 999 para parar): '))
    if numero == 999:
        break
    soma = soma + numero
    i = i + 1
print(f'A soma dos {i} valores é {soma}!')
