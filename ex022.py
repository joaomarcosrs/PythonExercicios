# Input do nome
nome = str(input('Digite o seu nome completo: ')).strip()
##Pode -se usar o método '.strip()' já no começo pra eliminar todos os espaços antes e depois da string

# Transformar todas as letras em maiúsculas
print('O nome em mmaisúculas: {}'.format(nome.upper()))

# Transformar todas as letras em minúsculas
print('O nome em minúsculas: {}'.format(nome.lower()))

# Split do nome para retirar os espaços, juntar e contar apenas as letras
nome_split = nome.split()
nome_join = ''.join(nome_split)
#teste nome função join
#print(nome_join)
print('O nome tem {} letras'.format(len(nome_join)))

# Contar apenas as letras do primeiro nome
print('O primeiro nome tem {} letras'.format(len(nome_split[0])))

#######################################################################
#Versão do Professor
#nome = str(input('Digite seu nome completo: ')).strip()
#print('Analisando seu nome...')
#print('Seu nome em maiúsculas é {}'.format(nome.upper()))
#print('Seu nome em minúsculas é {}'.format(nome.lower()))
#print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
