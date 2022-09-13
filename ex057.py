sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()
    if sexo != 'M' and sexo != 'F':
        print('ERRO! Digite (M) para masculino e (F) para feminino')
if sexo == 'M':
  print('O sexo digitado foi Masculino!')
else:
  print('O sexo digitado foi Feminino!')
print('FIM')