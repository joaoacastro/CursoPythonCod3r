nomes = ('Mayara', 'Milena', 'Bia', 'Gui', 'Ana')

# print('bia' in nomes) imprime como false, pois ele identifica letras maiusculas e minusculas

print('Bia' in nomes) # imprime como true
print(nomes[2]) # imprime o nome na posição 2, no caso imprime Gui, ja que se inicia em zero.
print('1')
"""
x = ('Bia')
print(type(x)) imprime o typo de classe que é nomes, no caso imprime <class 'str'> que é uma string
x = ('Bia',)
print(type(x)) imprime o type de classe que é nomes, no caso imprime <class 'tuple'>, só com a virgula ja se le como um tuple
"""
print('2')
print(type(nomes)) # imprime o type de classe que é nomes, no caso imprime <class 'tuple'>

print(nomes[1:3]) # imprime os "valores" segundo e terceiro sem incluir o quarto, no caso imprime ('Milena', 'Bia')
print(nomes[1:-1]) # imprime os valores da posição 1 até o penúltimo, no caso imprime ('Milena', 'Bia', 'Gui')
print(nomes[:-2]) #imprime todos os valores até o penúltimo (*sem incluir o penúltimo), imprime ('Mayara', 'Milena', 'Bia')

print(len(nomes)) #imprime a quantidade de elementos que tem na tupla