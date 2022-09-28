print(f'{"-=-" * 15}'
      f'\n{"BANCO DJANGO":^45}'
      f'\n{"-=-" * 15}')

saque = int(input('Qual o valor do saque? '))
i = 0
cedula = 50

while True:

    if saque >= cedula:
        saque = saque - cedula
        i = i + 1
    else:
        if i > 0:
            print(f'\nTotal de {i} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        i = 0
        if saque == 0:
            break

print(f'===' * 15)
print('Volte sempre, tenha um Bom Dia!!!')
