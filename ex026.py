frase = str(input('Digite uma frase: ')).strip().lower()

print('Existe(m) {} letras \'a\' na frase'.format(frase.count('a')))
print('O primeiro \'a\' está na posição {}'.format(frase.find('a') + 1))
print('O último \'a\' está na posição {}'.format(frase.rfind('a') + 1))



