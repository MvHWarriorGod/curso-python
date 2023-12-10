from random import choice
# lista
palabras =['perro', 'gato', 'rosa', 'mariposa', 'casa', 'arbol', 'pajaro', 'pescado', 'libro', 'computadora', 'celular', 'television', 'ventana', 'puerta', 'silla', 'mesa', 'cama', 'almohada', 'cobija', 'pantalon', 'camisa', 'zapatos', 'calcetines', 'panties', 'blusa', 'falda', 'vestido', 'sombrero', 'gorra', 'lentes', 'aretes', 'collar', 'pulsera', 'anillo', 'reloj', 'cartera', 'monedero', 'cinturon', 'corbata', 'corbata', 'chamarra', 'abrigo', 'bufanda', 'guantes', 'paraguas', 'maleta', 'mochila', 'l']

# elegir palabra aleatoria
def elegir_palabra_aleatoria(lista_palabras):
    return choice(lista_palabras)

# pedir letra
def pedir_letra():
    letra = input("Ingresa  una letra: ")
    return letra


# checquear letra
def checar_letra(palabra, letra):
    if letra in palabra:
        return True
    else:
        return False



# si es correcta, mostrarla en letra
def mostrar_letra(palabra, letra, letras_imprimir ):       

    for index in range(len(palabra)):
        
        if palabra[index] == letra:
            
           letras_imprimir[index]=letra   

    cadena_resultante = ' '.join(letras_imprimir)                
    print(cadena_resultante)
                           
    if '-' not in letras_imprimir:
        print("Ganaste")
        exit()
   
    print("\n")


# jugar
def jugar():
    palabra = elegir_palabra_aleatoria(palabras)
    # print(palabra)  
    letras_imprimir=[]

    if len(letras_imprimir)==0:
        for letter in palabra:
            letras_imprimir.append('-')

    print(' '.join(letras_imprimir))
    while True:
        letra = pedir_letra()
        letra = letra.lower()
        if checar_letra(palabra, letra):

            mostrar_letra(palabra, letra, letras_imprimir)
        else:
            print("La letra no está en la palabra")
            break

jugar()