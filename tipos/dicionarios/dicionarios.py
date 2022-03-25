aluno = {
    'nome': 'Enrico Castro',
    'idade': 10,
    'nota': 8.9,
    'sexo': 'Masculino',
    'cursos': ['Inglês','Espanhol','Italiano']
}

print(type(aluno))
print(aluno['nome']) # print Enrico Castro
print(aluno['nota']) # print 8.9
print(aluno['cursos']) # print ['Inglês', 'Espanhol', 'Italiano']

print(aluno.keys()) # print dict_keys(['nome', 'idade', 'nota', 'sexo', 'cursos'])
print(aluno.values()) # print dict_values(['Enrico Castro', 10, 8.9, 'Masc.', ['Inglês', 'Espanhol', 'Italiano']])

print(len(aluno)) # print a quantidade de keys no dicionario, no caso print 5

print(aluno.items()) # print todos os items do dicionario, no caso print dict_items([('nome', 'Enrico Castro'), ('idade', 10), ('nota', 8.9), ('sexo', 'Masc.'), ('cursos', ['Inglês', 'Espanhol', 'Italiano'])])
print(aluno.get('sexo')) # print Masculino
#print(aluno.get('cidade')) # não da erro, porém print none
print(aluno.get('cidade','São Paulo'))
print(aluno.get('tags',[])) # neste caso quando a propriedade não existir, no caso a tags, retorna como default