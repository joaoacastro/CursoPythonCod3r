frase = 'Python É Uma Linguagem Bacana!'
print('py' in frase) # print como False, pois da diferença de maiusculos para minusculos
print('py' not in frase) # print como True
print('ing' in frase)   # print como True
print(len(frase)) # print o tamanho de caracteres da frase, neste caso print 30
print(frase.lower()) # print tudo minúsculo, python é uma linguagem bacana!
print(frase.upper()) # print tudo maiúsculo, PYTHON É UMA LINGUAGEM BACANA!

print('py' in frase.lower()) # print como True, pois diferente da linha 2, agora para a comparação está toda a frase em minúsculo
print(frase.split()) # .plit() quebra todos os espaços em brancos e divide com virgulas, no caso print ['Python', 'É', 'Uma', 'Linguagem', 'Bacana!']

fraseNova = frase.upper()
print(fraseNova.split('A')) # quebra todos as letras 'A' da string, no caso print ['PYTHON É UM', ' LINGU', 'GEM B', 'C', 'N', '!']

