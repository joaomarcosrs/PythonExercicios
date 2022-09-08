frase = str(input("Digite uma frase: "))
new_frase = frase.upper().strip().split()
teste_palindromo = ''.join(new_frase)
inv_palindromo = ''

for i in range(len(teste_palindromo) - 1, -1, -1):
  inv_palindromo = inv_palindromo + teste_palindromo[i]

print(f'\nO inverso de {teste_palindromo} é {inv_palindromo}')
if teste_palindromo == inv_palindromo:
  print(f'A frase \033[1;32m{frase}\033[0m é um PALÍNDROMO')
else:
  print(f'A frase \033[1;31m{frase}\033[0m NÃO é um PALÍDROMO')


#Usar o método reversed() seria mais eficiente.