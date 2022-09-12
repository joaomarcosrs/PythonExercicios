# for i in range(1, 10):
#     print(i)
# print('FIM')

# i = 1
# while i < 10:
#     print(i)
#     i = i + 1
# print('FIM')

# n = 1
# while n != 0:
#     n = int(input('Digite um valor: '))
# print('FIM')

# r = 'S'
# while r == 'S':
#     n = int(input('Digite um valor: '))
#     r = str(input('Quer continuar? [S/N]: ')).upper().strip()
# print('FIM')

n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print(f'Você digitou {par} númeross pares e {impar} números ímpares')
