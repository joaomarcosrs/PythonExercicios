lst_terms = []
new_terms = 1

termo = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão da progressão: '))
pri_termo = termo

print(f'\n{"=" * 40}\n'
      f'{"Progressão Aritmética":^40}\n'
      f'{"=" * 40}\n')

print(f'O 1° termo é: {pri_termo:>3}\n'
      f'A razão é: {razao:>6}\n'
      f'Os 10 primeiros termos da PA são:\n')

print(pri_termo, end=' ')
i = 0
while i < 9:
    termo = termo + razao
    print(f'{termo}', end=' ')
    lst_terms.append(str(termo))
    i = i + 1

    if i == 9:
        while new_terms != 0:
            new_terms = int(input(f'\n\nVocê gostaria de ver mais quantos termos?'
                                  f'\nDigite 0 caso deseje encerrar: '))
            c = i
            if new_terms != 0:
                while (c + new_terms) > i:
                    termo = termo + razao
                    lst_terms.append(str(termo))
                    i = i + 1
                print(f'\33[33m{" ".join(lst_terms)}\33[0m')
print(f'\n\nFim do Programa')
