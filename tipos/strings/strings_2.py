nome = 'Thais Carla'
print(nome[0])  # print T
print(nome[-3]) # print r
print(nome[6:]) # print Carla
print(nome[:5]) # print Thais, entra o indice 0, 1, 2, 3, 4, como neste caso e nos outros o indice 5 não entra

print(nome[3:7]) # print is C, começa no indice 3 até o 7, porém o indice 7 não entra

numeros = '1234567890'
print(numeros[::])  # como não foi identificado o indice para iniciar e finalizar ele imprimi todos os numeros
print(numeros[::2]) # sem a identificação do indice para iniciar e para finalizar, porém com o indice para ir pulando, neste caso de 2 em 2 -> 13579
print(numeros[1::2]) # print 24680, indo de 2 em 2 apartir do indice 1
print(numeros[::-1]) # inverte a string, no caso print 0987654321
print(numeros[::-2]) # neste caso ele inverte a string pulando de 2 em 2

print(nome[::-1]) # inverte a string, no caso print alraC siahT