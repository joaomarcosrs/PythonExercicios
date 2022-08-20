nome = str(input('Digite o nome completo da pessoa: ')).strip()

nome_tit = nome.title()

if 'Silva' in nome_tit:
    print('A pessoa tem Silva no nome!')
else:
    print('A pessoa não tem Silva no nome!')