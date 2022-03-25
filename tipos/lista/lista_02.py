lista = [1, 5, 'Rebeca', 'Guilherme', 3.1415]
print(lista.index('Guilherme')) # print a posição dele na lista, no caso print 3, pois está no indice 3
#print(lista.index(42)) # print erro => ValueError: 42 is not in list, pois tentamos acessar um indice que não está na lista

print(lista[2]) # print Rebeca
print(1 in lista) # print True
print('Rebeca' in lista) # print True
print('Pedro' in lista) # print False
print('Pedro' not in lista) # print True

print(lista[0]) # print 1
#print(lista[5]) # erro, print IndexError: list index out of range, ou seja, o indice está fora da lista

print(lista[-1]) # print o ultimo elemento da lista, no caso, print 3.1415
print(lista[-5]) # print de tras para frente o 5 elemento, no caso, print 1
#print(lista[-6]) # erro, print IndexError: list index out of range, ou seja, o indice está fora da lista

