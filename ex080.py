lst_numero = list()

for i in range(0, 5):
    numero = int(input('Digite um valor: '))
    if i == 0 or numero > max(lst_numero):
        lst_numero.append(numero)
        print('Adicionado no final da lista...')
    else:
        c = 0
        while c < len(lst_numero):
            if numero <= lst_numero[c]:
                lst_numero.insert(c, numero)
                print(f'Adicionado na posição {c} da lista...')
                break
            c = c + 1
print(f'{"-=-"*15}')
print(f'Os valores digitados em ordem foram {lst_numero}')

