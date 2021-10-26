"""
INTEGRANTES: 
    ESTEBAN TORRES
    MARCOS TORO 
    NEIFER GOODSOON
    RONALD MADARIAGA
"""
"""
● El sistema de envío debe ser un programa que pregunta qué tipo de envío es necesario (Rápido 
o largo)
● Si es un envío a una distancia de más de 1.000 km es considerado largo. Si es igual o menor a la 
distancia de 1.000 km es considerado rápido. 
● En el caso que sea un envío rápido debe enviarse a una Bodega_A, caso contrario debe ser 
almacenado a una Bodega_B.
● El programa debe verificar que cada bodega no supere las 500 unidades
0"""
import os

# VARIABLES GLOBALES
dicc_Recorridos = {
    'A' : {'distancia' : 0,'stock': 0 , 'movimientos':[] },
    'B' : {'distancia' : 0 , 'stock':0, 'movimientos':[]}
}
#print(dicc_Recorriodos[1000]['stock'])
# FUNCIONES

def tipo_envio(diccionario:dict):
    distancia = int(input('Ingrese la distacia del envío: '))
    if distancia > 1000:
        print('EL VIAJE ES LARGO')
        print('ENVIAR A BODEGA_B')
        diccionario['B']['distancia'] += distancia
        stock = int(input('Ingresa el stock a enviar: '))
        diccionario['B']['movimientos'].append(stock)
        diccionario['B']['stock'] += stock
        if  diccionario['B']['stock']  <= 500:
            print('Se puede realizar el envio a bodega B')         
        else: 
            print('La bodega no puede superar las 500 unidades')
            diccionario['B']['stock'] -= stock
            diccionario['B']['distancia'] -= distancia
    elif distancia <= 1000:
        print('VIAJE RÁPIDO')
        print('ENVIAR A BODEGA_A')
        diccionario['A']['distancia'] += distancia
        stock = int(input('Ingresa el stock a enviar: '))
        diccionario['B']['movimientos'].append(stock)
        diccionario['A']['stock'] += stock
        if  diccionario['A']['stock'] <= 500:
            print('Se puede realizar el envio a bodega A') 
        else: 
            print('La bodega no puede superar las 500 unidades')
            diccionario['A']['stock'] -= stock
            diccionario['A']['distancia'] -= distancia
    return tipo_envio



#Funcion que limpia la pantalla
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

# funcion para mostrar los usuarios registrados en la aplicación 
def mostrar_recorridos(Diccionario:dict): # FUNCION PARA MOSTRAR LOS CLIENTES REGISTRADOS EN LA APLICACION 
    print('LISTADO DE RECORRIDOS')
    print('------------------------------')         
   #Recorremos la lista de usuarios
    for clave, valor in Diccionario.items(): # SE RECORREN LAS CLAVES Y VALORES DEL DICCIONARIO 
       distancia = valor['distancia'] # SE ASIGNA EL VALOR DE LA CLAVE 'BODEGA' DEL DICCIONARIO RECORRIDOS A BODEGA
       stock = valor['stock'] # SE ASIGNA EL VALOR DE LA CLAVE 'STOCK' DEL DICCIONARIO DATOS A STOCK
       print(f'Para la bodega {clave}, se enviaron {stock} unidades y se recorrieron {distancia} km')
       
    print('')
    print('')      
    continuar = input('Presiona ENTER para continuar.....')
    clearConsole()
    return Diccionario


# INICIO
while True:
    clearConsole() 
    print('-------------------------------------------')
    print('------------------ MENU -------------------')
    print('-------------------------------------------')
    print('1. Planificar recorrido')
    print('2. Mostrar registro de recorridos')
    print('3. Salir del programa')
    print('')
    print('--------SELECCIONE UNA OPCION-------------')
    opcion = input('Seleccione una opcion---> ')
    print('------------------------------------------')   
    clearConsole()
    if opcion == '1':
        print(dicc_Recorridos)
        tipo_envio(dicc_Recorridos)
        print(dicc_Recorridos)
    elif opcion == '2':
        print(dicc_Recorridos)
        mostrar_recorridos(dicc_Recorridos)
        print(dicc_Recorridos)
    elif opcion == '3':
        break
    else: 
       print('--------------------------------')
       print('ingrese una opcion correcta: ')
       print('--------------------------------')
# FIN