nome = str(input('Digite o nome completo de uma pessoa: ')).strip()

nome_split = nome.split()

nome_ult = len(nome_split) - 1

#print(nome_split)
#print(nome_ult)

print('O primeiro nome da pessoa é: {}'.format(nome_split[0]))
print('O último nome da pessoa é: {}'.format(nome_split[nome_ult]))
