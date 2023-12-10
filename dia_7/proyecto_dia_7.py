class Persona:
  def __init__(self, nombre, apellidos):
    self.nombre = nombre
    self.apellidos = apellidos

class Cliente(Persona):
  def __init__(self, nombre, apellidos, nro_cuenta, balance):
    super().__init__(nombre, apellidos)
    self.nro_cuenta = nro_cuenta
    self.balance = balance    

  def __str__(self):
    return f'Nombre: {self.nombre} {self.apellidos}, Nro. Cuenta: {self.nro_cuenta}, Balance: {self.balance}'

  def depositar(self, monto):
    self.balance += monto
    print(f'Su nuevo balance es: {self.balance}')
    opcion=0

  def retirar(self, monto):
    if self.balance >= monto:
      self.balance -= monto
      print(f'Su nuevo balance es: {self.balance}')
      opcion=0
    else:
      print('No tiene fondos suficientes para realizar esta operación')
      opcion=0


def crear_cliente():
  nombre = input('Ingrese su nombre: ')
  apellidos = input('Ingrese sus apellidos: ')
  nro_cuenta = input('Ingrese su número de cuenta: ')
  balance = float(input('Ingrese su balance: '))
  cliente = Cliente(nombre, apellidos, nro_cuenta, balance)
  return cliente      

def inicio():

  opcion=0

  cliente = crear_cliente()
  print(cliente)
  for opcion in range(0,3):
    print('*'*50)
    print('Bienvenido al Banco ABC')
    print('*'*50)
    print('1. Depositar')
    print('2. Retirar')
    print('3. Salir')
  
    opcion = input('Ingrese una opción: ')
    
    if opcion == '1':
      monto = float(input('Ingrese el monto a depositar: '))
      cliente.depositar(monto)
    elif opcion == '2':
      monto = float(input('Ingrese el monto a retirar: '))
      cliente.retirar(monto)
    elif opcion == '3':
      print('Gracias por preferirnos')
    else:
      print('Opción incorrecta')

inicio()