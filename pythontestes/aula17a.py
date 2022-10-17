num = (2, 5, 9)
# num[2] = 3 #Isso não vai ser possível assim, pois a Tupla é imutável
print(num)

#############################################################################################
num = [2, 5, 9]
num[2] = 3 #Como a Lista é mutável, dessa forma é possível fazer as alterações na lista
print(num)

# Porém eu não consigo utilizar o mesmo comando para adicionar novos elementos, algo como:
# num[3] = 4
# Para isso, é necessário utilizar o método append()
num.append(7)
print(num)

#############################################################################################
num = [8, 3, 2, 5, 9]
num.append(7)
print(num)

num.sort()
print(num)

num.sort(reverse=True)
print(num)

#################################################################################################
num = [8, 3, 2, 5, 9]
num.append(7)
print(num)
print(sorted(num))
num.insert(2, 0)
print(num)

################################################################################################
num = [8, 3, 2, 5, 9]
num.append(7)
print(num)
print(sorted(num))
num.insert(2, 0)
print(num)
num.pop()
print(num)
num.pop(2)
print(num)

#18 minutos pausado
