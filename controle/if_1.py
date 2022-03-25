nota = float(input('Informe a nota do aluno (de 0 a 10): '))
comportado = True if input ('Comportado (y/n): ') == 'y' else False

if nota >= 9 and comportado:
    print(f'Parabéns, sua nota foi de {nota} e você entrou para o nosso quadro de Honra!')
elif nota >= 6: # elif = else if
    print(f'Show, sua nota foi {nota}, continue estudando, na próxima você entra em nosso quadro de Honra!')
    if comportado == True and nota >= 6:
        print('Obs.: Continue sendo esse aluno(a) comportado que você foi! =)')
else:
    print(f'Sua nota foi {nota}, e infelizmente você está reprovado! =(')
    if comportado == True and nota < 6:
        print('Obs.: Continue sendo esse aluno(a) comportado que você foi! =)')