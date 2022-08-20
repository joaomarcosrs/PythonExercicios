
#Teste inicial condicional IF
# nome = str(input('Qual o seu nome? '))
# if nome != 'João':
#     print('Seu nome é tão normal!')
# else:
#     print('Que nome lindo você tem!')
# print('Bom dia, {}!'.format(nome))


#Teste condicional: Notas escolares
nota_first = float(input('Digite a primeira nota do aluno: '))
nota_secon = float(input('Digite a segunda nota do aluno: '))
media = (nota_first + nota_secon) / 2
print('Média: {:.1f} \nAluno Aprovado!'.format(media) if media >= 7 else 'Média: {:.1f} \nAluno Reprovado!'.format(media))
