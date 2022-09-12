# importando o método mean() da biblioetca numpy
from numpy import mean

# Listas
lst_nome = []
lst_idade = []
lst_sexo = []
index_sexo_masc = []
index_idade_fem = []

# laço para receber as informações do utilizador e armazenar nas respectivas listas
for i in range(1, 5):
    print(f'{"-"*5}{i}ª PESSOA{"-"*5}')
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo (M/F): ')).upper().strip()
    lst_nome.append(nome)
    lst_idade.append(idade)
    lst_sexo.append(sexo[:1])  # O append aqui é executado apenas na primeira letra do sexo

# teste para descobrir se as listas estavam sendo alimentadas
# print(lst_nome, lst_idade, lst_sexo)

# laço executado até a quantidade de nomes alimentados na lista
for i in range(len(lst_nome)):
    # a primeira condição serve para alimentar uma nova lista com apenas a idade dos homens
    if lst_sexo[i] == 'M':
        index_sexo_masc.append(lst_idade[i])
    # a segunda condição serve para alimentar uma lista apenas com a idade das mulheres abaixo de 20 anos
    if lst_sexo[i] == 'F' and lst_idade[i] < 20:
        index_idade_fem.append(lst_idade[i])

# Pega-se apenas o maior valor da idade
idade_max_masc = max(index_sexo_masc)
# usa-se o método index() para capturar o índice na lista de idade e, por tanto, saber o nome do homem mais velho
index_idade_max_masc = lst_idade.index(idade_max_masc)

# primeira parte do desafio que consiste em saber a média de idade dos membros das listas
print(f'A média das idades do grupo é {mean(lst_idade)} anos.')

#segunda parte do desafio é descobrir o homem mais velho e a sua respectiva idade
print(f'O {lst_nome[index_idade_max_masc]} é o homem mais velho com {lst_idade[index_idade_max_masc]} anos!')

# Conta-se aqui quantas mulheres existem com menos de 20 anos
print(f'Existe(m) {len(index_idade_fem)} mulher(es) com menos de 20 anos!')
