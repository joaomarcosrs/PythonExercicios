#from math import pow, sqrt
from math import hypot

cat_adj = float(input('Digite o valor do cateto adjacente: '))
cat_opo = float(input('Digite o valor do cateto oposto: '))

#hipot = pow(cat_adj, 2) + pow(cat_opo, 2)
#hipot_sqrt = sqrt(hipot)
hipotenusa = hypot(cat_adj, cat_opo)

print('O valor da hipotenusa é: {:.2f}'. format(hipotenusa))