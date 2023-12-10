palabra ='python'
lista=[]
# lista  =[letra for letra in palabra] #compresion de listas
# lista  =[ n/2 for n in range(0,21,2)] #compresion de listas de numeros
# lista  =[ n for n in range(0,21,2) if( n * 2 > 10)] #compresion de listas de numeros
# lista  =[ n  if n * 2 > 10 else 'no'  for n in range(0,21,2) ] #compresion de listas de numeros
    # lista.append(letra)
# print(lista)
 
pies=[10,20,30,40,50]
metros=[p* 3.281 for p in pies]
print(metros)