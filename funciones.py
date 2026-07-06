def leer_opcion():
    while True:
        try:
            opcion=int(input('Ingrese opción: '))
            if opcion >= 1 and opcion <= 7:
                return opcion
            else:
                print('Debe seleccionar una opción válida.')
        except ValueError:
            print('Debe ingresar un número entero.')

def validar_codigo(codigo, productos):
    codigo = codigo.strip().upper()
    return codigo != '' and codigo not in productos

def validar_nombre(nombre):
    return nombre.strip() != ''

def validar_categoria(categoria):
    return categoria.strip() != ''

def validar_precio(precio):
    return precio > 0

def validar_disponible(opcion):
    opcion = opcion.lower()
    return opcion == 's' or opcion == 'n'

def validar_stock(stock):
    return stock >= 0

def validar_vendidos(vendidos):
    return vendidos >= 0

def stock_categoria(categoria,productos,inventario):
    categoria=categoria.strip().lower()
    total=0
    for codigo in productos:
        datos_producto=productos[codigo]
        if datos_producto[1].strip().lower() == categoria:
            total+=inventario[codigo][0]
    print('El total de stock disponible es:',total)

def buscar_precio(precio_min,precio_max,productos,inventario):
    pass

def buscar_codigo(codigo,productos):
    codigo=codigo.strip().upper()
    return codigo in productos

def actualizar_precio(codigo,nuevo_precio,productos):
    codigo=codigo.strip().upper()
    if buscar_codigo(codigo,productos):
        productos[codigo][2]=nuevo_precio
        return True
    return False

def agregar_producto(codigo,nombre,categoria,precio,disponible,stock,vendidos,productos,inventario):
    pass

def eliminar_producto(codigo,productos,inventario):
    codigo=codigo.strip().upper()
    if buscar_codigo(codigo,productos):
        del productos[codigo]
        del inventario[codigo]
        return True
    return False

def mostrar_productos(productos,inventario):
    if len(productos) == 0 or len(inventario):
        print('Sin registros de productos')
    else:
        print('--- LISTA DE PRODUCTOS ---')
        for codigo in productos:
            datos_producto=productos[codigo]
            datos_inventario=inventario[codigo]

            print('CÓDIGO:',codigo)
            print('-'*26)
            print('Nombre:', datos_producto[0])
            print('Categoría:', datos_producto[1])
            print(f'Precio: ${datos_producto[2]}')
            print('Disponible:', datos_producto[3])
            print('Stock:', datos_inventario[0])
            print('Vendidos:', datos_inventario[1])
            print('-'*26)
            print()