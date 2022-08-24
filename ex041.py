from datetime import date

ano_nasc = int(input('Digite o ano de nascimento do atleta: '))
ano_corr = date.today().year
ano_diff = ano_corr - ano_nasc
print('\n')
if ano_diff <= 9:
  print('O atleta tem {} anos e pertence à categoria MIRIM!'.format(ano_diff))
elif ano_diff > 9 and ano_diff <= 14:
  print('O atleta tem {} anos e pertence à categoria INFANTIL!'.format(ano_diff))
elif ano_diff > 14 and ano_diff <= 19:
  print('O atleta tem {} anos e pertence à categoria JÚNIOR!'.format(ano_diff))
elif ano_diff > 19 and ano_diff <=20:
  print('O atleta tem {} anos e pertence à categoria SÊNIOR!'.format(ano_diff))
else:
  print('O atleta tem {} anos e pertence à categoria MASTER!'.format(ano_diff))