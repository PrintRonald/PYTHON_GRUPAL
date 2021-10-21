
print('---INGRESANDO_PROVEEDORES---')

info_proveedor = {}
while True:
    print('---OPCIONES---')
    print("""
    [1] Ingresar proveedor
    [2] Eliminar proveedor
    [3] Mostrar proveedores
    [4] Guardar Información
    [5] Salir del programa
    """)
    n = int(input('Ingrese una opción --> '))

    if n == 1:
        IDproveedor = input('Ingrese el identificador del proveedor: ')
        info_proveedor[IDproveedor] = {}
        Nombre_proveedor = input('Ingrese el nombre de la empresa proveedora: ')
        info_proveedor[IDproveedor]['Nombre'] = Nombre_proveedor
        Rut_proveedor = input('Ingrese el rut del proveedor: ')
        info_proveedor[IDproveedor]['Rut proveedor'] = Rut_proveedor
    elif n == 2:
        IDproveedor = input('Ingrese el identificador del proovedoor a eliminar: ')
        del info_proveedor[IDproveedor]
    elif n == 3:
        print(info_proveedor)
    elif n == 4:
        pass
    elif n == 5:
        break
    else:
        print('Ingrese una opción correcta')


