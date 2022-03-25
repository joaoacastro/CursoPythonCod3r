# Operador de membro
lista = [1, 2, 3, 'Ana', 'Carla']
2 in lista  # True
'Ana' not in lista  # False

# Operador de Identidade
x = 3
y = x
z = 3
x is z  # True
y is z  # True
x is not z  # False

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]
lista_a is lista_b  # True
lista_b is lista_c  # False, pois diferente do exemplo da linha 11, são iguais, porém não apontam para o mesmo local, fica mais facil de entender utilizando o python preview (extensão vscode)   # noqa
lista_c is lista_a  # True
