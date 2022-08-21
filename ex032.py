from datetime import date

ano = int(input('Digite um ano, porém se quiser analisar o ano atual digite 0: '))

if ano == 0:
    ano = date.today().year

div_four = ano % 4
div_hund = ano % 100
div_fourhun = ano % 400

if div_four == 0 and div_hund != 0 or div_four == 0 and div_hund == 0 and div_fourhun == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))


# print(div_four)
# print(div_hund)
# print(div_fourhun)
# print(resto)
