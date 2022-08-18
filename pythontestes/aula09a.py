frase = 'Curso em vídeo Python'
print(frase)

print(frase[::2])

print(frase.lower().count('p'))

print(frase)

print(len(frase))

print('Curso' in frase)

print(frase[:2])

print(frase[2:])

new_frase = frase[:2] + 'm' + frase[3:]
print(new_frase)

dividido = frase.split()
print(dividido)
print(dividido[0])