
"""
Control de Bodega 
Nuestro programa deberá tener las siguientes funciones:
- Crear una bodega virtual con los productos iniciales.
- Almacenar nuevos productos.
- Actualizar el stock de productos en la bodega virtual.
- Mostrar y retornar las unidades disponibles por producto.
- Mostrar y retornar las unidades disponibles de un producto en particular.
- Mostrar y retornar todos los productos de la tienda.
- Mostrar y retornar los productos que tienen más de un número de unidades (el usuario puede
escoger el número de unidades).
"""
"""
Control de Ventas
Nuestro programa deberá tener las siguientes funciones:
- mostrar y retornar el número de clientes registrados en la tienda.
- Funcionalidad para solicitar compra. Se ingresa el id del cliente, id del producto a comprar y las
unidades a comprar.
- respecto a la funcionalidad anterior, por defecto se comprará una unidad.
- Funcionalidad que verifique si existe stock necesario. Retorna valores booleanos.
- Funcionalidad que autoriza la compra. No es necesario que actualicen el stock de la bodega
virtual.
- Imprimir y retornar un mensaje “Compra aprobada y en camino” en caso que exista el stock
necesario.
- Imprimir y retornar un mensaje “Compra cancelada” en caso que no exista el stock necesario.
● Recuerden comentar debidamente su código.
"""
"""
PRODUCTOS: 
ZAPATILLAS: 20 PARES
POLERAS: 10 UNIDADES
ZAPATOS: 15 PARES
POLERÓN: 3 UNIDADES
CHAQUETA: 5 UNIDADES
GUANTES: 4 PARES
"""
#VARIABLES
diccionarioProductos1 ={  # se asignan las claves y valores al diccionarioProductos
        'zapatilla':20,
        'poleras' : 10,
        'zapatos' : 15,
        'poleron' : 3,
        'chaqueta' : 5,
        'guantes' : 4
    } 

# FUNCIONES

def crear_bodega(): # cremos bodega con productos iniciales
  global diccionarioProductos # la variable diccionarioProductos se define de manera global (¿funciona esta variable para todo el código? si funciona para todo el código)
  diccionarioProductos ={  # se asignan las claves y valores al diccionarioProductos
        'zapatilla':20,
        'poleras' : 10,
        'zapatos' : 15,
        'poleron' : 3,
        'chaqueta' : 5,
        'guantes' : 4
    } 
  #print(diccionarioProductos) # se imprime el diccionarioProductos
  return diccionarioProductos # esta funcion nos retorna el diccionarioProductos

def almacenar_producto(numero_productos:int): # creamos la funcion almacenar productos con un input de la funcion que es numero_productos que debe ser un numero entero
    bodega = {} # creamos el diccionario bodega
    for producto in range(numero_productos): # recorremos con la variable producto el rango que definimos com input en la función almacenar_producto(numero_producto:int)
        nombre_producto = input('ingrese el nombre del producto:') # creamos la variable nombre_producto donde pedimos al usuario ingresar el nombre del producto 
        stock_producto = input(f'ingrese el stock de {nombre_producto}: ') # creamos la variable stock_producto donde pedimos al usuario ingresar el stock del producto
        bodega[nombre_producto] = stock_producto # se agregan al diccionario bodega como clave el nombre_producto y como valor el stock_producto
    return bodega # de esta función se retorna el diccionario bodega

def actualizar_stock(ProductosActualizados:dict): # creamos la funcion actualizar_stock con un input de la funcion que es productoActualizados que debe ser un tipo de dato dict
    nombre_producto = input('ingrese el nombre del producto a actualizar: ') # se ingres nombre producto
    stock_producto = input(f'ingrese el nuevo stock {nombre_producto}: ') # se ingres nombre producto
    if (nombre_producto in ProductosActualizados): # se comprueba si el producto ingresado esta en el diccionarioProductos
            ProductosActualizados[nombre_producto] = stock_producto # si el producto se encuentra en nuestro diccionario ProductosActualizados se actualiza
    else:
        print('El producto no existe...') # si no se encuantra en este diccionario se arroja una alerta
        
    return 'Los datos se han actualizado correctamente' # se retorna un mensaje de exito en caso de actualizar correctamente el diccinario

def unidades_disponibles(diccionario:dict): # se crea la funcion unidades_disponibles con un input diccionario que debe ser de tipo dict
    for clave, valor in diccionario.items(): # se recorre con la varible clave, valor el diccinairo ingresado como input en la funcion unidades_disponibles
        print(f'El producto {clave} tiene {valor} unidades disponibles') # se imprime un mensaje por cada dato que contenga este diccionario
    return 'Se han mostrado los productos disponibles' # se retorna un mensaje de exito

a =unidades_disponibles(crear_bodega()) # 

print(a)


#   
#
##Inicio
#print('--------CONTROL BODEGA----------')
#diccionarioProductos = crear_bodega()
#while True:
#    print('---OPCIONES---')
#    print("""
#    [1] Almacenar Nuevos productos
#    [2] Actualizar stock de productos
#    [3] Mostrar y retornar las unidades disponibles
#    [4] Mostrar y retornar las unidades disponibles de un producto
#    [5] Mostrar y retornar todos los productos
#    [6] Mostrar y retornar todos los productos con mas 10 unidades
#    """)
#    n = int(input('Ingrese una opción --> '))
#    if n == 1:
#        cantidad_producto = int(input('Cuantos productos desea almacenar'))
#        diccionarioProductos.update(almacenar_producto(cantidad_producto))
#        print(diccionarioProductos)
#    elif n == 2:
#        actualizar_stock(diccionarioProductos)
#        print(diccionarioProductos) 
#    elif n == 3:
#       pass
#    elif n == 4:
#       pass
#    elif n == 5:
#      pass
#    elif n == 6:
#        break
#    else:
#        print('Ingrese una opción correcta')
#


# Fin



