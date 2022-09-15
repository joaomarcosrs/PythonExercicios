sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('ERRO! Digite (M) para masculino e (F) para feminino')
if sexo == 'M':
  print('O sexo digitado foi Masculino!')
else:
  print('O sexo digitado foi Feminino!')
print('FIM')

# ###################### Solução do Professor ###########################
# sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
# while sexo not in 'MmFf':
#     sexo = str(input('Dados Iválidos. Por favor, infrme seu sexo: ')).strip().upper()[0]
# print(f'Sexo {sexo} regstrado com sucesso!')
