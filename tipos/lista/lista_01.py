lista = []
print(lista) # print [], ou seja, a lista está vazia

lista.append(1)
lista.append(5)
lista.append('Ana')
lista.append('Beatriz')
print(lista) # como adicionamos itens, neste momento a lista print [1, 5, 'Ana', 'Beatriz'], lembrando que não é aconselhável misturar itens em uma mesma lista

lista.remove('Ana')
print(lista) # como removemos um item, neste momento a lista print [1, 5, 'Beatriz']

lista.reverse()
print(lista) # print como na linha anterior nós invertemos, então nossa lista agora print ['Beatriz', 5, 1]
