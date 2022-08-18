algo = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'
      '\nSó tem espaços? {}'
      '\nÉ um número? {}'
      '\nÉ alfabético? {}'
      '\nÉ alfanumérico? {}'
      '\nEstá em maiúsculas? {}'
      '\nEstá em minúsuclas? {}'
      '\nEstá capitalizada? {}'
      ''.format(type(algo),
                algo.isspace(),
                algo.isnumeric(),
                algo.isalpha(),
                algo.isalnum(),
                algo.isupper(),
                algo.islower(),
                algo.istitle()))
