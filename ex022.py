
# Input do nome
nome = input('Digite o seu nome completo: ')

# Transformar todas as letras em maiúsculas
print(nome.upper())

# Transformar todas as letras em minúsculas
print(nome.lower())

# Split do nome para retirar os espaços, juntar e contar apenas as letras
nome_spliit = nome.split()
nome_join = ''.join(nome_spliit)
print(nome_join)
print(len(nome_join))

# Contar apenas as letras do primeiro nome
print(len(nome_spliit[0]))