from re import sub


def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    return a / b


def resto_divisao(a, b):
    return a % b


# fn => função, op1 => operador 1, op2 => operador 2
def operacao_aritmetica(fn, op1, op2):
    return fn(op1, op2)


result_soma = operacao_aritmetica(soma, 13, 38)
result_subtracao = operacao_aritmetica(subtracao, 40, 27)
result_multipl = operacao_aritmetica(multiplicacao, 4, 47)
result_divisao = operacao_aritmetica(divisao, 450, 71)
result_resto_divisao = operacao_aritmetica(resto_divisao, 450, 71)

print(f"resultado da soma: {result_soma} \n resultado da subtração: {result_subtracao} \n resultado da multiplicação {result_multipl} \n resultado da divisão: {result_divisao} \n resultado do resto da divisão {result_resto_divisao}")


def soma_parcial(a):
    # processamento pesado 1 -> demora 10s
    # processamento pesado 2 -> demora 10s
    # processamento pesado 3 -> demora 40s
    # demora um total de 1min
    def concluir_soma(b):
        return a + b  # -> demora 10s
    return concluir_soma

# r1 = soma_total(1, 2) -> demora 1m10s
# r2 = soma_total(1, 3) -> demora 1m10s
# r3 = soma_total(1, 4) -> demora 1m10s
# neste exemplo demoraria 3min30s para concluir o codigo


soma_1 = soma_parcial(1)  # 1min
r1 = soma_1(2)  # 10seg
r2 = soma_1(3)  # 10seg
r3 = soma_1(4)  # 10seg
# neste exemplo demoraria 1min30s para concluir o codigo

resul_final = soma_parcial(10)(12)
print(resul_final)
