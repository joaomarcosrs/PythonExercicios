sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()
    if sexo != 'M' and sexo != 'F':
        print('ERRO! Digite (M) para masculino e (F) para feminino')
print('FIM')
