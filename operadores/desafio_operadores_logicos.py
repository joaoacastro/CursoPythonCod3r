trab_terca = False
trab_quinta = False

if(trab_terca and trab_quinta):
    print('Parabéns, você concluiu os dois trabalhos, tem direito a TV de 50" e o Sorvete!')    # noqa

elif(trab_terca or trab_quinta):
    print('Parabéns, você concluiu um dos trabalhos, logo tem direito a TV de 32" e o Sorvete!')    # noqa

elif(not trab_terca and not trab_quinta):
    print('Que pena como você não concluiu nenhum trabalho então não tem direito a ganhar nem a TV nem o Sorvete =(')   # noqa

"""
Pode-se fazer também da seguinte forma:
trab_terca = True
trab_quinta = True

tv_50 = trab_terca and trab_quinta
sorvete = trab_terca or trab_quinta
tv_32 = trab_terca != trab_quinta   # != => ou exclusivo, como no caso não pode-se usar xor   # noqa
mais_saudavel = not sorvete

print("Tv50={} Tv32={} Sorvete={} Saudável={} "
    .format(tv_50, tv_32, sorvete, mais_saudavel))   # noqa
"""
