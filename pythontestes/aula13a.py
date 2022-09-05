#Escreve "Oi!" de 0 até 5
for i in range(0, 6):
    print('Oi!')
print('Fim')

#Escreve "Oi!" de 1 até 5
for i in range(1, 6):
    print('Oi!')
print('Fim')

#Escreve de 6 até 1, uma contagem regressiva diminuindo uma unidade
for i in range(6, 0, -1):
    print(i)
print('Fim')

#Escreve de 0 até 8 pulando dois números, a saída é:
#0, 2, 4, 6, 8
for i in range(0, 10, 2):
    print(i)
print('Fim')

#Nesse exemplo, usa-se o argumento de numero + 1, para o contador incluir o numero digitado pelo usuário
numero =  int(input('Digite um número'))
for i in range(0, numero+1):
    print(i)
print('Fim!')

#Nesse exemplo, o usuário define o início, fim e o pulo do contador, como anteriormente, o fim é somado com 1, para poder incluir o número digitado pelo usuário.
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for i in range(inicio, fim + 1, passo):
    print(i)
print('Fim!')

#Nesse exemplo, é execuado um somátório com tamanho 4, teste da nova formatação do python, melhor que o método format()
s = 0
for i in range(0, 4):
    n = int(input('Digite um  valor: '))
    s = s + n
print(f'O somotário dos valores é {s:.1f}')