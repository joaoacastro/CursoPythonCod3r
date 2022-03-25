# for i in range(10):
#     print(i) #retorna de 0 a 9

# for i in range(1, 11):
#     print(i) #retorna de 1 a 10

# for i in range(1, 100, 7):
#     print(i) #imprimi do 1 ao 100, indo de 7 em 7, finalizou em 99

# for i in range(20, 0, -3):
#     print(i) #imprimi do 20 ao 0, indo de 3 em 3, inicia em 20, finalizou em 2

# nums = [2, 4, 6, 8]

# for n in nums:
#     print(n)
#     #imprimi
#     # 2
#     # 4
#     # 6
#     # 8

# for n in nums:
#     print(n, end=',') #imprimi 2,4,6,8

# for n in nums:
#     print(n, end=' ') #imprimi 2 4 6 8

# texto = 'Python é muito top!'

# for letra in texto:
#     print(letra, end= ' ')

# for n in {1, 2, 3, 4, 4, 4}:
#     print(n, end= ' ') #imprimi 1 2 3 4, pois ele não aceita duplicação

produto = {
    'Nome': 'Caneta',
    'Valor': 7.95,
    'Desconto': 0.5
}

for k in produto: # k => key, ou seja, a chave/atributo, no caso seria o produto
    print(k,':',produto[k]) #imprimi conforme descrito acima

for k, valor in produto.items(): # k => key, ou seja, a chave/atributo, no caso seria o produto
    print(k, ':', valor) #imprimi conforme descrito acima

for valor in produto.values():
    print(valor, end=' ') #imprimi Caneta 7.95 0.5

for k in produto.keys():
    print(k, end=' ') #imprimi Nome Valor Desconto