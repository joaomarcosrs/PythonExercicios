1from datetime import date

lst_nome = []
lst_ano_nasc = []
lst_idade = []
ano = date.today().year

for i in range(0, 7):
  nome = str(input('Digite o nome da pessoa: ')).strip()
  ano_nasc = int(input('Digite o ano de nascimento: '))
  lst_nome.append(nome)
  lst_ano_nasc.append(ano_nasc)
  lst_idade.append(ano - lst_ano_nasc[i])

for i in range(0, 7):
  if lst_idade[i] < 18:
    print(f'\n{lst_nome[i]} nasceu no ano de {lst_ano_nasc[i]}\n'
          f'Ele(a) tem {lst_idade[i]} ano(s).\n'
          f'{lst_nome[i]} ainda é menor de idade\n\n')
  else:
    print(f'\n{lst_nome[i]} nasceu no ano de {lst_ano_nasc[i]}\n'
          f'Ele(a) tem {lst_idade[i]} ano(s).\n'
          f'{lst_nome[i]} é maior de idade\n\n')
