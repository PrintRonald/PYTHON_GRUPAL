"""
INTEGRANTES: 
    ESTEBAN TORRES
    MARCOS TORO 
    NEIFER GOODSOON
    RONALD MADARIAGA
"""
"""
● Debe crear una base de datos que tenga información de clientes: ID, nombre, apellido, edad y 
contraseña. Cree 4 clientes iniciales para probar el programa.
● Diseñe tres funciones: 
- la primera debe agregar nuevos clientes, 
- la segunda debe eliminar clientes según ID.
- la tercera debe mostrar toda la información por cliente.
 """
import os
#---------------VARIABLES-----------------#
#Creamos una base de datos con 4 clientes
clientes ={ '15.833.757-6':{'nombre':'Esteban','apellido':'Torres','edad':39,'contrasena':'123455'}
           ,'15.586.082-3':{'nombre':'Marcos','apellido':'Toro','edad':38,'contrasena':'123455'}
           ,'27.427.232-3':{'nombre':'Neifer','apellido':'Gonzalez','edad':18,'contrasena':'123455'}
           ,'18.659.284-0':{'nombre':'Ronald','apellido':'Madariaga','edad':27,'contrasena':'123455'}
          }

#---------------FUNCIONES-----------------# 
#Funcion que limpia la pantalla
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


#Funcion creada para agregar los clientes
def agregaCliente (usuarioDic:dict):
  datos ={}  
  print('AGREGAR DATOS DEL CLIENTE')
  print('---------------------------')
  print('')    
  rut = input('Ingrese el RUT (XX.XXX.XXX-X): ')
  nombre = input('Ingrese el nombre: ')
  apellido = input ('Ingrese el apellido: ')
  edad = input('Ingrese la edad: ')
  contrasena = input ('Ingrese la contraseña: ')

  #Creamos el diccionario leyendo las variables y asignando los valores
  for variable in ["nombre", "apellido","edad","contrasena"]:
      datos[variable] = eval(variable)
      

  #Agregamos el diccionario de datos al diccionario maestro
  print(datos)
  usuarioDic[rut] = datos
  print('Cliente Agregado Satisfactoriamente')
  print(' ')
  continuar = input('Presiona ENTER para continuar.....')
  clearConsole()

  return 'Clente agregado satisfactoriamente'



def eliminaCliente (clientes:dict):
  print('INGRESE USUARIO A ELIMINAR')
  print('---------------------------')        
  print ('')  
  rut = input('RUT (XX.XXX.XXX-X): ')

  if (rut in clientes):
     #mostramos los datos a eliminar
     print(f'El usuario eliminado es: {clientes[rut]}')
     print('')    
     del clientes[rut]

  else:
     print('ALERTA : El usuario no existe...')
    
  continuar = input('Presiona ENTER para continuar.....')
  clearConsole()
  return clientes 

#Funcion que muestra los datos de los clientes
def mostrarCliente (clientes:dict):
   print('LISTADO DE CLIENTES EXISTENTES')
   print('------------------------------')         
   #Recorremos la lista de usuarios
   for clave, valor in clientes.items():
       print(f'El Rut:{clave}.- {valor}')
       
   print('')
   print('')      
   continuar = input('Presiona ENTER para continuar.....')
   clearConsole()
   return clientes
#------------------INICO DEL PROGRAMA------------------#

while True: 
    print('-------------------------------------------')
    print('------------------ MENU -------------------')
    print('-------------------------------------------')
    print('1. Agregar un cliente')
    print('2. Eliminar a un cliente')
    print('3. Mostrar lista de clientes')
    print('4. Salir del programa')
    print('')
    print('--------SELECCIONE UNA OPCION-------------')
    opcion = input('Seleccione una opcion---> ')
    print('------------------------------------------')   
    clearConsole()
    if opcion == '1':
       #Llamamos y agregamos inmeditamente el nuevo cliente 
      agregaCliente(clientes)
      print(clientes)
    elif opcion == '2':
      eliminaCliente(clientes)
      print(clientes)
    elif opcion =='3':
      mostrarCliente(clientes)
    elif opcion == '4':
      break
    else: 
       print('--------------------------------')
       print('ingrese una opcion correcta: ')
       print('--------------------------------')

#---------------FIN DEL PROGRAMA--------------------#

