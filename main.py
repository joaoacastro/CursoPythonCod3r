from funcoes import basico  # ou import funcoes.basico
import funcoes.map_reduce
"""
import pacote.sub.arquivo

print('primeiro arquivo')
print(__name__) #essa variavel mostra o nome do arquivo, no caso imprime __main__
print(__package__) #essa variavel mostra a pasta do arquivo, no caso imprime None
"""
"""
podemos importar desta maneira -> import tipos.variaveis <- porém podemos importar também como mostra o exemplo abaixo
"""
# from tipos import variaveis, basicos
# from tipos import lista
# import tipos.tuplas
# import tipos.conjuntos
# import tipos.dicionarios

# import operadores.unarios
# import operadores.aritmeticos
# import operadores.relacionais
# import operadores.atribuicao
# import operadores.logicos
# import operadores.ternario

# import controle.if_1
# import controle.if_2
# import controle.for_1
# import controle.while_1
# import controle.outros_exemplos

# basico.saudacao() imprimi Bom Dia!
# se utilizar from funcoes.basico import saudacao
# saudacao() também imprimi Bom Dia!
# basico.saudacao() # imprimi Bom dia Pessoa! Você nem parece ter 20 anos!
# basico.saudacao('Mayara') # imprimi Bom dia Mayara. Você nem parece ter 20 anos!
# basico.saudacao('Bruthus', 10) #imprimi Bom dia Bruthus. Você nem parece ter 10 anos!
# basico.saudacao(idade=58) #imprimi Bom dia Pessoa! Você nem parece ter 58 anos!
# basico.saudacao() # imprimi Boa Tarde, ou seja, o segundo identificador sobrescreveu o primeiro.
# basico.soma_e_multi(x=10, a=2, b=3) #não imprimi nada pois a função está retornando apenas e não imprimindo, para imprimir deve armazenar a função em uma variavel e imprimir apartir deassa variavel conforme abaixo
# a = basico.soma_e_multi(x=10, a=2, b=3)
# b = basico.soma_e_multi(x=20, a=3, b=7)
# resultado = a + b
# print(resultado)

# from funcoes import args
# s = args.soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(s)
# resultado = args.resultado_final(nome='Pedro', nota = 7.3)
# print(resultado)

# from funcoes import funcional
