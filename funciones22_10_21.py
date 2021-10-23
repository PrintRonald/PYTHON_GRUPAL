
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


# FUNCIONES

def crear_bodega():
  global diccionarioProductos
  diccionarioProductos ={
        'zapatilla':20,
        'poleras' : 10,
        'zapatos' : 15,
        'poleron' : 3,
        'chaqueta' : 5,
        'guantes' : 4
    } 
  print(diccionarioProductos)
  return diccionarioProductos

def almacenar_producto(numero_productos):
    bodega = {}
    for producto in range(numero_productos):
        nombre_producto = input('ingrese el nombre del producto:')
        stock_producto = input('ingrese el stock del producto: ')
        bodega[nombre_producto] = stock_producto
    return bodega #crear bodega retorna un diccionario

def actualizar_stock(diccionarioProductos):
    nombre_producto = input('ingrese el nombre del producto a actualizar: ')
    stock_producto = input('ingrese el nuevo stock: ')
    try:
        if (nombre_producto in diccionarioProductos):
            diccionarioProductos[nombre_producto] = stock_producto
        else:
            print('El producto no existe...')
    except:
        print('El producto no existe...')
        
    return diccionarioProductos

def unidades_disponibles():
    print(diccionarioProductos)
    return 

    

#Inicio
print('--------CONTROL BODEGA----------')
diccionarioProductos = crear_bodega()
while True:
    print('---OPCIONES---')
    print("""
    [1] Almacenar Nuevos productos
    [2] Actualizar stock de productos
    [3] Mostrar y retornar las unidades disponibles
    [4] Mostrar y retornar las unidades disponibles de un producto
    [5] Mostrar y retornar todos los productos
    [6] Mostrar y retornar todos los productos con mas 10 unidades
    """)
    n = int(input('Ingrese una opción --> '))
    if n == 1:
        cantidad_producto = int(input('Cuantos productos desea almacenar'))
        diccionarioProductos.update(almacenar_producto(cantidad_producto))
        print(diccionarioProductos)
    elif n == 2:
        actualizar_stock(diccionarioProductos)
        print(diccionarioProductos) 
    elif n == 3:
       pass
    elif n == 4:
       pass
    elif n == 5:
      pass
    elif n == 6:
        break
    else:
        print('Ingrese una opción correcta')




# Fin



