"""
INTEGRANTES: 
    ESTEBAN TORRES
    MARCOS TORO 
    NEIFER GOODSOON
    RONALD MADARIAGA
"""
"""
● Guarde la información de los productos en una bodega virtual. 
● Los productos son vasos, cucharas, cuchillos y tenedores. Cada producto debe tener un stock 
aleatorio entre 300 y 500 unidades y una descripción del producto.
● Debe definir funciones que puedan: 
● Sumar y disminuir el número de unidades por producto. 
● Agregar nuevos productos. 
● Quitar productos de la bodega virtual.
● Mostrar todos los productos disponibles y su stock. Debe tener un desfase de un segundo entre 
cada producto.
● Verificar si un producto tiene menos de 400 unidades y enviar una alerta.
"""
import random
import time
import os

#Funcion que limpia la pantalla
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

# Funcion bodega virtual
diccionarioProductos ={  
        'vasos': { 'stock': random.randrange(300,500), 'descripción': 'Vasos de vidrio reciclado'},
        'cucharas' : { 'stock': random.randrange(300,500), 'descripción': 'Cuchara de metal reciclado'},
        'cuchillos' : { 'stock': random.randrange(300,500), 'descripción': 'Cuchillo de metal reciclado'},
        'tenedores' : { 'stock': random.randrange(300,500), 'descripción': 'Tenedor de metal reciclado'}
}

def mostrar_bodega(diccionario:dict):
    print('LISTADO DE PRODUCTOS EXISTENTES')
    print('------------------------------')         
    #Recorremos la lista de usuarios
    for clave, valor in diccionario.items():
       print(f'{clave}---> {valor}')
       
    print('')
    print('')      
    continuar = input('Presiona ENTER para continuar.....')
    clearConsole()
    return diccionario

#print(diccionarioProductos)
#mostrar_bodega(diccionarioProductos)
#print(diccionarioProductos)




# función sumar numero de unidades por producto

def sumar_unidades(diccionario:dict, stock:str):
    print('INGRESE A QUE PRODUCTO LE SUMA UNIDADES')
    print('---------------------------')        
    print ('')  
    producto = input('PRODUCTO: ')

    if (producto in diccionario):
        cantidad = int(input('Undidades que va a sumar: '))
        diccionario[producto][stock] += cantidad
    else:
        print('ALERTA : El producto no existe..')
    
    print('')
    print('')      
    continuar = input('Presiona ENTER para continuar.....')
    clearConsole()
    return 'Suma unidades con exitovas'

#print(diccionarioProductos)
#sumar_unidades(diccionarioProductos,'stock')
#print(diccionarioProductos)

# función restar numero de unidades por producto

def restar_unidades(diccionario:dict, stock:str):
    print('INGRESE A QUE PRODUCTO LE RESTAR UNIDADES')
    print('---------------------------')        
    print ('')  
    producto = input('PRODUCTO: ')

    if (producto in diccionario):
        cantidad = int(input('Undidades que va a restar: '))
        if diccionario[producto][stock] <= cantidad :
            print('ALERTA : No se puede quitar esta cantidad de unidades...')
        else: 
            diccionario[producto][stock] -= cantidad
    else:
        print('ALERTA : El producto no existe...')
    
    print('')
    print('')      
    continuar = input('Presiona ENTER para continuar.....')
    clearConsole()
    return 'Resta unidades con exito'

#print(diccionarioProductos)
#restar_unidades(diccionarioProductos,'stock')
#print(diccionarioProductos)


# función nuevos productos

def nuevos_productos(diccionario:dict):
    print('INGRESE UN NUEVO PRODUCTO')
    print('------------------------------') 
    nombre = input('Ingrese el nombre del producto: ')
    diccionario[nombre] = {}
    stock = int(input('Ingrese el stock del producto: '))
    diccionario[nombre]['stock'] = stock
    descripcion = str(input('Ingrese una descripción del producto: '))
    diccionario[nombre]['descripción'] = descripcion
    
    continuar = input('Presiona ENTER para continuar.....')
    clearConsole()
    return 'se agrega con exito'

#print(diccionarioProductos)
#nuevos_productos(diccionarioProductos)
#print(diccionarioProductos)
           

# función quitar productos de la vodefa

def quitar_productos(diccionario:dict):
    print('INGRESE PRODUCTO A ELIMINAR')
    print('---------------------------')        
    print ('')  
    nombre = input('Ingrese el nombre del producto a eliminar: ')
    if (nombre in diccionario):
        del diccionario[nombre] 
    else:
        print('ALERTA : El producto no existe...')
    
    continuar = input('Presiona ENTER para continuar.....')
    clearConsole()   
    return 'Eliminado con exito'

#print(diccionarioProductos)
#quitar_productos(diccionarioProductos)
#print(diccionarioProductos)

# función para mostrar todos los productos y su stock con desfase de 1 segundo 

def mostrar_stock(diccionario:dict):
    print('LISTADO DE PRODUCTOS EXISTENTES')
    print('------------------------------') 
    for clave, valor in diccionario.items():
        stock = valor['stock']
        print(f' El producto {clave}, tiene {stock} unidades') 
        time.sleep(1)

    print('')
    print('')      
    continuar = input('Presiona ENTER para continuar.....')
    clearConsole()
    return 'Mostrado con exito'

#print(diccionarioProductos)
#mostrar_stock(diccionarioProductos)
#print(diccionarioProductos)

# función para verificar si un producto tiene menos de 400 unidades

def alerta(diccionario:dict, stock:str):
    print('VERIFICACIÓN')
    print('------------------------------') 
    producto = input('Que producto desea verificar: ')
    if (producto in diccionario):
        if diccionario[producto][stock] <= 400:
            print('No hay suficiente inventario...')
        else:
            print('Hay suficiente stock en bodega...')
    else:
        print('El producto no existe...')


    print('')
    print('')      
    continuar = input('Presiona ENTER para continuar.....')
    clearConsole()
    return 'No hay suficitente inventario...'

#print(diccionarioProductos)
#alerta(diccionarioProductos,'stock')
#print(diccionarioProductos)

    

# INICIO 
while True: 
    print('-------------------------------------------')
    print('------------------ MENU -------------------')
    print('-------------------------------------------')
    print('1. Mostrar bodega')
    print('2. Sumar unidades a un producto')
    print('3. Restar unidades a un producto')
    print('4. Agregar nuevos productos')
    print('5. Eliminar productos de bodega')
    print('6. Mostrar el stock de cada producto')
    print('7. Verificar si hay menos de 400 unidades en stock por producto')
    print('8. Salir del programa')
    print('--------SELECCIONE UNA OPCION-------------')
    opcion = input('Seleccione una opcion---> ')
    print('------------------------------------------')   
    clearConsole()
    if opcion == '1':
       print(diccionarioProductos)
       mostrar_bodega(diccionarioProductos)
       print(diccionarioProductos)
    elif opcion == '2':
        print(diccionarioProductos)
        sumar_unidades(diccionarioProductos,'stock')
        print(diccionarioProductos)
    elif opcion =='3':
        print(diccionarioProductos)
        restar_unidades(diccionarioProductos,'stock')
        print(diccionarioProductos)
    elif opcion =='4':
        print(diccionarioProductos)
        nuevos_productos(diccionarioProductos)
        print(diccionarioProductos)
    elif opcion =='5':
        print(diccionarioProductos)
        quitar_productos(diccionarioProductos)
        print(diccionarioProductos)
    elif opcion =='6':
        print(diccionarioProductos)
        mostrar_stock(diccionarioProductos)
        print(diccionarioProductos)
    elif opcion =='7':
        print(diccionarioProductos)
        alerta(diccionarioProductos,'stock')
        print(diccionarioProductos)
    elif opcion =='8':
      break
    else: 
       print('--------------------------------')
       print('ingrese una opcion correcta: ')
       print('--------------------------------')





# FIN 





