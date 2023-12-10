# def generador_numeros():
#     numero = 0
#     while True:
#         numero += 1
#         yield numero

# def encapsular_generador(generador_numeros,areas):
#     print('*'*100)
#     print('su turno es')
#     if areas == 'P':
#       numero=next(generador_numeros)
#       print(f'P-{ numero}')
#     elif areas == 'F':
#       numero=next(generador_numeros)
#       print(f'F-{ numero}')
#     else:
#       numero=next(generador_numeros)
#       print(f'C-{ numero}')
#     print('*'*100)

def numeros_perfumeria():
    for numero in range(1, 1000000):
        yield f'P-{numero}'

def numeros_farmacia():
    for numero in range(1, 1000000):
        yield f'F-{numero}'

def numeros_cosmeticos():
    for numero in range(1, 1000000):
        yield f'C-{numero}'

p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmeticos()

def decorador(rubro):
    print('\n')
    print('*'*100)
    print('su turno es')
    if(rubro == 'P'):
        print(next(p))
    elif(rubro == 'F'):
        print(next(f))
    else:
        print(next(c))
    print('Aguarde y sera antendido')    
    print('*'*100)            

  