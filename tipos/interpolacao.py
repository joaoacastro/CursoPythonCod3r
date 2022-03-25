from string import Template

nome, idade, sexo = 'Ana', 30, 'feminino'

print('Nome: %s Idade: %d Sexo: %s' % (nome, idade, sexo)) # print Nome: Ana Idade: 30 Sexo: feminino, idade retorna como 30 e ignora as casas decimais, pois o %d imprimi apenas a parte inteira, para imprimir a parte quebrada, utilizar %f -> 1f de float
    #se for utilizar %f, você consegue limitar a quantas casas decimais quiser, utilizando da seguinte forma %.2f, neste caso limitaria a duas casas decimais e faz o arredondamento.

print('Nome: {0} Idade: {1}'.format(nome, idade)) # print Nome: Ana Idade: 30
print(f'Nome: {nome} Idade: {idade} Sexo: {sexo}') # print Nome: Ana Idade: 30 Sexo: feminino

s = Template('Nome: $n Idade: $i')
print(s.substitute(n=nome, i=idade)) # print Nome: Ana Idade: 30, porém neste caso, deve-se importar template from string linha 1