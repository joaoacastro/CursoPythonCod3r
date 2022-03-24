pessoas = ['Turin', 'Igara']
adjs = ['Fofo', 'Peludo']

for p in pessoas:
    for a in adjs:
        print(f'{p} é {a}!')

for i in [1, 2, 3]:
    pass

for i in range(1 ,11):
    if i % 2:
        continue
    print(i) # imprimi apenas os números pares de 1 a 10

for i in range(1, 11):
    if i == 5:
        break
    print(i) # imprimi os valores de 1 a 4, pois quanto iguala a 5 ele para