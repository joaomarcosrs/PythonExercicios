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

########################## SOLUÇÃO PROFESSOR ###########################
# palavras = (
#     "aprender", 'programar',
#     'linguagem', 'python',
#     'curso', 'estudar',
#     'praticar', 'trabalhar',
#     'mercado', 'programador',
#     'futuro')
#
# for p in palavras:
#     print(f'\n Na palavra {p.upper()} temos ', end='')
#     for letra in p:
#         if letra.lower() in 'aeiou':
#             print(letra, end=' ')
