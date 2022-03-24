lockdown = False
grana = 30

status = 'Continuar em casa' if lockdown or grana <= 100 else 'Uhuuuul, partiu rolee'

print(f'Com o Lockdown {lockdown} e a grana R${grana}, o status atual é: {status}')