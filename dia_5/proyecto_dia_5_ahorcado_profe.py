from random import choice

palabras =['perro', 'gato', 'rosa', 'mariposa', 'casa', 'arbol', 'pajaro', 'pescado', 'libro', 'computadora', 'celular', 'television', 'ventana', 'puerta', 'silla', 'mesa', 'cama', 'almohada', 'cobija', 'pantalon', 'camisa', 'zapatos', 'calcetines', 'panties', 'blusa', 'falda', 'vestido', 'sombrero', 'gorra', 'lentes', 'aretes', 'collar', 'pulsera', 'anillo', 'reloj', 'cartera', 'monedero', 'cinturon', 'corbata', 'corbata', 'chamarra', 'abrigo', 'bufanda', 'guantes', 'paraguas', 'maleta', 'mochila', 'l']

letras_correctas=[]
letras_incurrectas=[]
intentos=6
aciertos=0
juego_terminado=False


def elegir_palabra(lista_palabras):
    palabra_elegida= choice(lista_palabras)
    letras_unicas=len(set(palabra_elegida))

    return palabra_elegida, letras_unicas

def pedir_letra():
    letra_elegida=''
    es_valida=False
    abcedario='abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida=input("Ingresa una letra: ").lower()
        if letra_elegida in abcedario and len(letra_elegida)==1:
            es_valida=True
        else:
            print("Ingresa una letra valida")

    return letra_elegida

def mostrar_nuevo_tablero(palabra_elegida):

    lista_oculta=[]
    
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append("-")

    print(' '.join(lista_oculta))

def chequear_letra(letra_elegida, palabra_oculta, vidas , coincidencias):

    fin=False

    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias+=1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print("Ya habias elegido esta letra, intenta con otra diferente")

    else:
        letras_incurrectas.append(letra_elegida)
        vidas-=1
    
    if vidas==0:
        fin=perder()
    elif coincidencias==letras_unicas:
            fin=ganar(palabra_oculta)
    return vidas, fin,coincidencias


def perder():
    print("Ta has quedado sin vidas")
    print(f"La palabra oculta era: {palabra}")
    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("Felicidades has econtrado la palabra!!!!!!")
    return True

palabra, letras_unicas= elegir_palabra(palabras)

while not juego_terminado:
    print('\n' +'*'*20 + 'AHORCADO' + '*'*20+'\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('letras incorrectas:  '+ ' - '.join(letras_incurrectas))
    print(f"Vidas: {intentos}")
    letra=pedir_letra()
    intentos, terminado, aciertos=chequear_letra(letra, palabra, intentos, aciertos)
    juego_terminado=terminado
