

def checar_3_cigras(lista):
  list_3_cifras=[]
  for n in lista:
    if n in range(100,1000):
      list_3_cifras.append(n)
    else:
      pass
  return list_3_cifras

resultado= checar_3_cigras([126,359,1000])

print(resultado)