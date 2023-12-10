from random import shuffle
# lista inicial
palitos = ['-', '--', '---', '----',]

#  mezclar palitos
def mezclar_palitos(palitos):
    shuffle(palitos)
    return palitos

# pedir intento 

def probar_suerte():
    intento = ''

    while intento  not in ['1', '2', '3', '4']:
        intento = input("Ingrese un numero del 1 al 4: ")

    return int(intento)



# comprobar intento

def chequear_intento(palitos, intento):
    if palitos[intento-1] == '-':
        print("A lavar los platos")
    else:
        print('esta vez te has salvado')
    print(f'te ha tocado {palitos[intento-1]}')


# jugar
palitos_mezclados = mezclar_palitos(palitos)
intento = probar_suerte()
chequear_intento(palitos_mezclados, intento)