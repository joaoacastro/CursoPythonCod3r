from functools import reduce


def somar_nota(delta):
    def calc(nota):
        return nota + delta
    return calc


notas = [6.4, 7.2, 5.8, 8.4]
notas_finais = list(map(somar_nota(1.6), notas))

print(notas_finais)

total = 0
for n in notas:
    total += n
print(total)

# O EXEMPLO A CIMA E O ABAIXO IMPRIMEM O MESMO RESULTADO, POREM DE FORMAS DIFERENTES.


def somar(a, b):
    return a + b


# 1o parametro -> função | 2o parametro -> a lista | 3o parametro -> valor inicial
total = reduce(somar, notas, 0)
print(total)
# for i, nota in enumerate(notas):
#     notas[i] = nota + 1.5

# for i in range(len(notas)):
#     notas[i] = notas[i] + 1.5
