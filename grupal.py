#Este es un comentario realizado por Joao
print('---Bienvenido a la base de datos proveedores/contacto/transacciones---')

info_proveedor = {}
info_contacto={}
while True:
    print('---OPCIONES---')
    print("""
    [1] Ingresar proveedor
    [2] Eliminar proveedor
    [3] Mostrar proveedores
    [4] Ingresar contacto
    [5] Eliminar contacto
    [6] Mostrar Contactos
    [7] Salir del programa
    """)
    n = int(input('Ingrese una opción --> '))

    if n == 1:
        IDproveedor = input('Ingrese el identificador del proveedor: ')
        info_proveedor[IDproveedor] = {}
        Nombre_proveedor = input('Ingrese el nombre de la empresa proveedora: ')
        info_proveedor[IDproveedor]['Nombre Proveedor'] = Nombre_proveedor
        Rut_proveedor = input('Ingrese el rut del proveedor: ')
        info_proveedor[IDproveedor]['Rut proveedor'] = Rut_proveedor
    elif n == 2:
        IDproveedor = input('Ingrese el identificador del proovedoor a eliminar: ')
        del info_proveedor[IDproveedor]
    elif n == 3:
        print(info_proveedor)
    elif n == 4:
       IdContacto = input('Ingrese el ID de contacto: ')
       info_contacto[IdContacto]={}
       nombreContacto = input('Ingrese el nombre de contacto: ')
       info_contacto[IdContacto]['nombreContacto']= nombreContacto
       telefonoContacto=input('Ingrese el telefono de contacto: ')
       info_contacto[IdContacto]['Telefono Contacto']= telefonoContacto

    elif n == 5:
        IdContacto = input('Ingrese el identificador del contacto a eliminar: ')
        del info_contacto[IdContacto]
    elif n == 6:
        print(info_contacto)
    elif n ==7:
        break

    else:
        print('Ingrese una opción correcta')


