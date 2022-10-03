print(f'{"-=-"*15}\n'
      f'{"TABELA SÉRIE A 2022":^45}\n'
      f'{"-=-"*15}\n')
brasileirao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'América-MG', 'Fortaleza', 'Botafogo', 'Santos', 'Goiás', 'São Paulo', 'Bragantino', 'Coritiba', 'Ceará', 'Cuiabá', 'Avaí', 'Atlético-GO', 'Juventude')

print(f'Os cinco primeiros colocados no brasileirão são:')
i = 1
for time in range(0, 5):
  print(f'{i}º {brasileirao[time]}')
  i = i + 1

print(f'\nOs quatro últimos colocados no brasileirão são:')
i = len(brasileirao) - 3
for time in range(len(brasileirao) - 4, len(brasileirao)):
  print(f'{i}º {brasileirao[i - 1]}')
  i = i + 1

print(f'\nOs times em ordem alfabética:')
sorted_brasileirao = sorted(brasileirao)
for time in range(len(brasileirao)):
  print(sorted_brasileirao[time])

#No ano de 2022 a Chapecoense está na série B do Campeonato Brasileiro.
print(f'\nO time do Botafogo está na {brasileirao.index("Botafogo") + 1}ª posição')

#ótimos pontos de melhoria para esse programa