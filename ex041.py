from datetime import date

ano_nasc = int(input('Digite o ano de nascimento do atleta: '))
ano_corr = date.today().year
ano_diff = ano_corr - ano_nasc

print('\n')
print('O alteta possui {} anos'.format(ano_diff))
if ano_diff <= 9:
  print('Categoria MIRIM!')
elif ano_diff <= 14:
  print('Categoria INFANTIL!')
elif ano_diff <= 19:
  print('Categoria JÚNIOR!')
elif ano_diff <=20:
  print('Categoria SÊNIOR!')
else:
  print('Categoria MASTER!')
