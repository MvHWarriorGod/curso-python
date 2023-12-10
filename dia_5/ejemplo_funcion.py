precios_cafe=[('capuccino', 1.5), ('latte', 1.8), ('expresso', 1.2), ('moka', 2.0)]

# for cafe, precio in precios_cafe:
#     print(cafe,precio)

def cafe_mas_caro(precios_cafe):
    cafe_mas_caro=''
    precio_mayor=0
    for cafe, precio in precios_cafe:
        if precio > precio_mayor:
            precio_mayor=precio
            cafe_mas_caro=cafe
    return (cafe_mas_caro, precio_mayor)

# print(cafe_mas_caro(precios_cafe))
caffe, precio = cafe_mas_caro(precios_cafe)

print(f'el cafe mas caro es: {caffe} cuyo precio es {precio}')