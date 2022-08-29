from time import sleep

#Obter valores das retas do usuário
reta_um = float(input('Digite o valor da primeira reta: '))
reta_dois = float(input('Digite o valor da segunda reta: '))
reta_tres = float(input('Digite o valor da terceira reta: '))

#Conjunto de condições para verificar se as três retas forma um triângulo
cond_a = abs(reta_dois - reta_tres) < reta_um < reta_dois + reta_tres
cond_b = abs(reta_um - reta_tres) < reta_dois < reta_um + reta_tres
cond_c = abs(reta_um - reta_dois) < reta_tres < reta_um + reta_dois

#Conjunto de condições para definir qual o tipo de triângulo
equi = reta_um == reta_dois and reta_dois == reta_tres
isoc = reta_um == reta_dois and reta_dois != reta_tres or reta_um == reta_tres and reta_tres != reta_dois or reta_dois == reta_tres and reta_tres != reta_um
escal = reta_um != reta_dois and reta_dois != reta_tres and reta_um != reta_tres

print('\nVerificando se é um triângulo...')
sleep(2)

#A primeira condição verifica se ele é um triângulo, com base nass condições pré-definidas, se for um triângulo executa o bloco interno que está aninhado
if cond_a and cond_b and cond_c:
  print('\nÉ um triângulo!')
  sleep(1.5)
  print('Verificando qual triângulo é...')
  print('\n')
  sleep(2)
  #Bloco para definir que tipo de triângulo, com bas nas condições pré-estabelecidas
  if equi:
    print('As retas {:.2f}, {:.2f} e {:.2f} formam um triângulo EQUILATERO!'.format(reta_um, reta_dois, reta_tres))
  elif isoc:
    print('As retas {:.2f}, {:.2f} e {:.2f} formam um triângulo ISÓCELES!'.format(reta_um, reta_dois, reta_tres))
  else:
    print('As retas {:.2f}, {:.2f} e {:.2f} formam um triângulo ESCALENO!'.format(reta_um, reta_dois, reta_tres))
#Condição caso as retas não formem um triângulo.
else:
  print('\nAs retas {:.2f}, {:.2f} e {:.2f} não formam um triângulo!'.format(reta_um, reta_dois, reta_tres))
