pessoa = {
    'nome': 'Prof. Alberto',
    'idade': 43,
    'cursos': ['React', 'Python']
}

print(pessoa['idade']) # print 43
pessoa['cursos'].append('Angular')
print(pessoa) # print {'nome': 'Prof. Alberto', 'idade': 43, 'cursos': ['React', 'Python', 'Angular']}

pessoa.pop('idade') # o pop lê o valor e tira de dentro do dicionário
print(pessoa)

pessoa.update({'idade': 40, 'Sexo': 'masculino'})
print(pessoa)

del pessoa['cursos'] # exclui o par que esta indexado com a string cursos de dentro de pessoa
print(pessoa)

pessoa.clear()
print(pessoa) # o clear limpa todo o dicionário, ou seja, imprimi o dicionário vazio {}
