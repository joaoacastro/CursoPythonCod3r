a = 'valor' # True => retorna como existe
a = 0 # False => retorna como não existe, ou zero ou vazio
a = -0.00001 # True => retorna como existe
a = '' # False => retorna como não existe, ou zero ou vazio
a = ' ' # True => retorna como existe 
a = [] # False => retorna como não existe, ou zero ou vazio
a = {} # False => retorna como não existe, ou zero ou vazio

if a:
    print('Existe!!')
else:
    print('não existe ou zero ou vazio...')