cores = ('verde', 'amarelo', 'azul', 'azul', 'azul', 'branco')
print(type(cores)) # print class 'tuple'
print(cores[0]) # print verde
print(cores[-1]) # print branco
print(cores[1:]) # print ('amarelo', 'azul', 'azul', 'azul', 'branco')

print(cores.index('amarelo')) # print 1, pois é a posição do amarelo na tupla
print(cores.count('azul')) # print 3, pois é a quantidade de itens azul que tem nessa tupla

print(len(cores)) # print 6 pois é a quantidade de itens que tem nessa tupla