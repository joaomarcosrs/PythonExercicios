lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche[1])
print(lanche[2:])
print(lanche[-2])
print(lanche[-2:])
print(lanche[:2])

#Tuplas são imutáveis
print('\n\n')
for comida in lanche:
  print(f'Eu vou comer {comida}')

print('\n\n')
#Outra forma de fazer
for i in range(0, len(lanche)):
  print(f'Eu vou comer {lanche[i]}')

print('\n\n')
for pos, comida in(enumerate(lanche)):
  print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')
print('\n\n')

#Método Sorted()
lanche = sorted(lanche)
#Se fizer uma atribuição com uma mudança estrutural na Tupla, ela se torna uma lista
print(lanche)
#################################################################################################################################################################################################

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #Na concatenação de Tuplas a ordem irá importar, na soma de a + b, o resultado mostrado será uma tupla cos elementos da primeira tupla e depois os elementos da sengunda.
print(c)
print(len(c))
print(c.count(5)) # Retorna quantos números existem
print(c.index(8)) # Pega a primeira ocorrência do número
print(c.index(5, 2)) #Desta forma delimita a procura do valor, á partir de uma determinada posição (Deslocamento)
