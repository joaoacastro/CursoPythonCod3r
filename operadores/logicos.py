b1 = True
b2 = False
b3 = True

print (b1 and b2 and b3) # retorna como False, pois utilizando o and só será True se todos forem True
print(b1 or b2 or b3) # retorna como True, pois utilizando o or só precisa ter Trueb em uma das opções
print(b1 != b2) # o sinal de diferente é tratado neste caso como OU EXCLUSIVO (xor), ou seja, se neste caso...
                # ...b1 for diferente de b2 é um caso de OU EXCLUSIVO.
                # OU EXCLUSIVO => Exclusivamente um deles é verdadeiro e o outro falso.
print(not b1) # retorna como False
print(not b2) # retorna como True

print(b1 and not b2 and b3) # retorna como True, pois b1 = True, não b2 = o contrário de False, ou seja, True e b3 = True

x = 3
y = 4

print(b1 and not b2 and x < y) # retorna como true, pode "misturar" operadores racionais como operadores lógicos.