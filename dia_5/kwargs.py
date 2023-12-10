# def suma(**kwargs):
#     total = 0
#     for key, value in kwargs.items():
#         print(f"key: {key} value: {value}")
#         total += value
#     return total

# print(suma(a=1, b=2, c=3, d=4, e=50.9, f=100, g=20000))

def prueba(num1,num2, *args, **kwargs):
    print(f'el primer valor es: {num1}')
    print(f'el segundo valor es: {num2}')

    for arg in args:
        print(f'el valor es: {arg}')

    for key, value in kwargs.items():
        print(f'el valor de {key} es: {value}')

numeros = [1,2,3,4,5,6,7,8,9,10]
nombres = {'a':'juan', 'b':'pedro', 'c':'maria'}

prueba(15,20, *numeros, **nombres)