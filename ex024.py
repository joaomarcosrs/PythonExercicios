cidade = str(input('Digite o nome da cidade: ')).strip()
cidade_tit = cidade.title()


if cidade_tit[:5] == 'Santo':
    print('O nome da Cidade começa com a palavra Santo!')

else:
    print('O nome da Cidade não começa com a palavra Santo!')
