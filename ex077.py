tpl_palavras = (
    "aprender", 'programar',
    'linguagem', 'python',
    'curso', 'estudar',
    'praticar', 'trabalhar',
    'mercado', 'programador',
    'futuro')

for i in range(len(tpl_palavras)):
    print(f'Na palavra {tpl_palavras[i].upper()} temos ', end='')
    palavra = tuple(tpl_palavras[i])
    for vogal in range(len(palavra)):
        if palavra[vogal] in 'aeiou':
            print(palavra[vogal], end=' ')
    print('')
