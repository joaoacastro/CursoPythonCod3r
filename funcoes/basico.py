# def saudacao():
#     print('Bom Dia!')

# def saudacao_da_tarde():
#     print('Boa Tarde!')

# def saudacao(nome):
#     print(f'Bom dia {nome}!')

# def saudacao(nome = 'Pessoa'):
#     print(f'Bom dia {nome}!')

def saudacao(nome='Pessoa', idade=20):
    # \n quebra linha
    print(f'Bom dia {nome}! \n Você nem parece ter {idade} anos!')

# def saudacao():
#     print('Boa Tarde!')


def soma_e_multi(a, b, x):
    return a + b * x


if __name__ == '__main__':
    # imprimi Bom dia Ana! Você nem parece ter 8 anos! porém se eu chamar a função no main.py não irá imprimir, pois o if será false
    saudacao('Ana', idade=8)
