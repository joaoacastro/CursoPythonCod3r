a = 9
b = 5.5

print(a+b)

texto = 'Sua idade é...'
idade = 28

print(texto + str(idade)) #se nao colocarmos str (referente a string) dara erro, pois não tem como concatenar um texto (texto) com um numeral (idade)

print(f'{texto} {idade}') #imprime igual ao exemplo anterior, Sua idade é... 28

print(3*'bom dia ') #imprime 3 vezes a string bom dia, podemos fazer da seguinte forma para obter o mesmo resultado.

saudacao = 'bom dia '
print(3*saudacao) #imprime bom dia bom dia bom dia

# em Python não existe const, para definir uma constante utilizamos letras maiusculas.

PI = 3.14
raio = float(input('Informe o valor da Circ.?')) #colocamos o input dentro da variavel raio para salvar a informação preenchida no terminal, colocamos dentro de float para o valor inserido ser lido como numeral e não como string

area = PI * raio * raio # podemos utilizar o pow(power), no exemplo ficaria pow(raio,2), ou seja, raio elevador a 2

print(f'baseando no valor {raio} da circunferencia, o valor da area é de {area} m²')