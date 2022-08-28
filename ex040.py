nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1 + nota2) / 2
print('\n')
if media < 5.0:
  print('''Média: {:.1f}
Aluno Reprovado!'''.format(media))
elif media >= 5.0 and media < 7.0:  #Pode-se usar a sintaxe 7.0 > media <= 5.0
  print('''Média: {:.1f}
Aluno em Recuperação!'''.format(media))
else:
  print('''Média: {:.1f}
Aluno Aprovado!'''.format(media))