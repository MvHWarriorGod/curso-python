
from random import *



# aleatorio =   randint(1,50) #Genera un numero aleatorio entre 1 y 50
# aleatorio =   round(uniform(1,50),1) #Genera un numero aleatorio entre 1 y 50 con decimales redondeado a 1 decimal
# aleatorio =   random() #Genera un numero aleatorio entre 0 y 1
# colores =["azul", "rojo", "verde", "amarillo"]

# aleatorio =   choice(colores) #Genera un aleatorio de una lista

# print(aleatorio)

numeros = list(range(1,50,5))

shuffle(numeros) #Desordena una lista

print(numeros)