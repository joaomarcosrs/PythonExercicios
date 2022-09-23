lst_idade = []
lst_sexo = []
maior_idade_index = []
homens_index = []
menor_mulher_index = []
while True:
    print(f'\n{"-=-" * 15}\n'
          f'{"CADASTRE UMA PESSOA":^45}\n'
          f'{"-=-" * 15}')
    idade = int(input('\nDigite a idade: '))
    lst_idade.append(idade)
    while True:
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[:1]
        if sexo not in 'MF':
            print(f'Opção Inválida!!!\n'
                  f'Digite [M] para MASCULINO e [F] para FEMININO.')
        else:
            lst_sexo.append(sexo)
            break

    while True:
        keep_loop = str(input('Você deseja cadastrar outra pessoa [S/N]? ')).strip().upper()[:1]
        if keep_loop not in 'SN':
            print(f'\nOpção Inválida!!!\n'
                  f'Digite [S] para SIM e [N] para NÃO.\n')
        if keep_loop in 'SN':
            break

    if keep_loop in 'N':
        for i in range(len(lst_sexo)):
            if lst_idade[i] > 18:
                maior_idade_index.append(lst_idade[i])
            if lst_sexo[i] == 'M':
                homens_index.append(lst_sexo[i])
            if lst_sexo[i] == 'F' and lst_idade[i] < 20:
                menor_mulher_index.append(lst_idade[i])
        break
if len(menor_mulher_index) == 1:
    plu_sing = 'mulher'
else:
    plu_sing = 'mulheres'

print(f'\n{"=" * 15}FIM DO PROGRAMA{"=" * 15}\n\n'
      f'Total de pessoas com mais de 18 anos: {len(maior_idade_index)}\n'
      f'Ao todo temos {len(homens_index)} homens cadastrados\n'
      f'Temos {len(menor_mulher_index)} {plu_sing} com menos de 20 anos')
