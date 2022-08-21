nome = str(input('Qual é o seu nome? '))
if nome == 'João':
    print('Que nome bonito!')
elif nome == 'Gustavo' or nome == 'Pedro' or nome == 'Júnior':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))