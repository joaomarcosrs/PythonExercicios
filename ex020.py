import random
alunos = []

for i in range(4):
    nomes = input('Digite o nome do aluno: ')
    alunos.append(nomes)

ordem = random.sample(alunos, k=4)
print('A ordem de apresentação é {}'.format(ordem))



