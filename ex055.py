lst_nome = []
lst_peso = []

for i in range(0,3):
  nome = str(input('Digite o nome da pessoa: ')).strip()
  peso = str(input('Digite o peso da pessoa: ')).replace(',', '.')
  peso = float(peso)
  lst_nome.append(nome)
  lst_peso.append(peso)

indice_peso_max = lst_peso.index(max(lst_peso))
indice_peso_min = lst_peso.index(min(lst_peso))


print(f'\nNome: {lst_nome[indice_peso_max]}\n'
      f'Peso: {max(lst_peso)}Kg\n'
      f'MAIOR PESO!')
print(f'\nNome: {lst_nome[indice_peso_min]}\n'
      f'Peso: {min(lst_peso)}Kg\n'
      f'MENOR PESO!')