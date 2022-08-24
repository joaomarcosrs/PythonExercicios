from datetime import date

ano_nasc = int(input('Digite o seu ano de nascimento: '))
ano = date.today().year
ano_diff = ano - ano_nasc
tempo = abs(ano_diff - 18)
print('\n')

if ano_diff < 18:
  print('Você tem {} anos, ainda faltam {} ano(s) para se alistar ao serviço militar!'.format(ano_diff, tempo))
elif ano_diff == 18:
  print('Você tem {} anos e já está na hora de se alistar ao serviço militar!'.format(ano_diff))
else:
  print('Você tem {} anos e já passou o tempo do seu alistamento em {} ano(s)!'.format(ano_diff, tempo))