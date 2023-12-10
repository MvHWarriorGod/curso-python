from random import *


numero_ramdon = randint(1, 100)
numero_ingresado = 0

print(numero_ramdon)

intentos = 0
for i in range(8):
    numero_ingresado=int(input("Ingrese un numero del 1 al 100: "))
    intentos += 1
    if numero_ingresado>100 and numero_ingresado<1:
        print("Numero no permitido")
    if numero_ingresado > numero_ramdon or  numero_ingresado < numero_ramdon:
        print("Game over")   
    if numero_ingresado == numero_ramdon:
        print("Ganaste")
        print("Intento realizados: ", intentos)
        break

else:
    print("Perdiste")
    print("Intento realizados: ", intentos)   
   