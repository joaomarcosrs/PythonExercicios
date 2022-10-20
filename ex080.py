lst_numero = list()
i = 0

for i in range(0, 5):
    numero = int(input('Digite um valor: '))
    if i == 0:
        lst_numero.append(numero)
        print('Adicionado no final da lista...')
    else:
        for c in range(0, len(lst_numero)):
            if numero >= lst_numero[c]:
                lst_numero.insert(i, numero)
                p = i
                break
            else:
                lst_numero.insert(i - 1, numero)
                p = i - 1
                break
        print(f'Adicionado na posição {p} da lista...')


