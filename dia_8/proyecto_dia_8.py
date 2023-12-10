from numeros import  decorador

def elegir_area():
  print('Bienvenido a la Farmacia CyD, por favor elija el área a la que desea dirigirse')
  print('P - PERFUMERÍA')
  print('F - FARMACIA')
  print('C - COSMÉTICOS')
  area = input('Ingrese el área: ')
  return area

def turnos():
 
  pedir_turno = 'S'
  area = ''
  while pedir_turno == 'S':
    area = elegir_area()  
    decorador(area)
    pedir_turno = input('¿Desea pedir turno? (S/N): ') 

  
turnos()