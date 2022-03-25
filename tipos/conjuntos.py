a = {1, 2, 3}
print(type(a)) # print class 'set'

#print(a[0]) # erro, pois 'set' não aceita indice, print TypeError: 'set' object is not subscriptable

a = set('codddddd3r')
print(a) # print em ordem aleatória e não aceita repetição, no caso print {'d', 'r', 'o', 'c', '3'}

print('3' in a, 4 not in a) # print True True

print({1,2,3}=={3,2,1,3}) # print como True, pois os mesmos elementos estão presentes nos dois conjuntos, lembrando que em conjuntos a ordem e os números repetidos não importam

c1 = {1, 2}
c2 = {2, 3}
print(c1.union(c2)) # print {1, 2, 3}, ele mostra a união dos dois conjuntos, porém não substitui nenhum conjunto e como dito anteriormente em conjunto ele ignora repetição

print(c1.intersection(c2)) # print {2}, pois é o único elemento que pertence aos dois conjuntos

c1.update(c2)
print(c1) # print {1, 2, 3}, diferente do .union o .update realmente adiciona no conjunto, no caso adicionou os elementos do conjunto 2 no conjunto 1

print(c2 <= c1) # subconjunto, ou seja, c2 é subconjunto de c1, no caso print True, por conta do update anterior, ou seja, o c2 que tem o conjunto {1,2,3} tem o conjunto c1 dentro dele, se excluirmos o update esta informação print False
print(c2 >= c1) # print False, pois é o inverso do exemplo anterior

print({1, 2, 3} - {2}) # neste caso, ele print a diferença entre os conjuntos, print {1, 3}
print(c1 - c2) # print {1}
c1 -= {2}  # atribuição subtrativa, ou seja, como no exemplo nós tiramos o elemento 2 do conjunto c1
print(c1)   # print {1, 3}