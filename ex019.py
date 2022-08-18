from random import choice
alunos = []

for i in range(4):
    nome = input('Digite um nome: ')
    alunos.append(nome)

sorteado = choice(alunos)
print('Entre os alunos {}, o aluno sorteado foi o {}'.format(alunos, sorteado))
