######## AULA PASSADA ########
# i = 1
# while i <= 10:
#     print(i, end='')
#     i = i + 1
# print('Acabou')

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s = s + n
print(f'A soma vale {s}')
