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
    pass

def buscar_precio(precio_min,precio_max,productos,inventario):
    pass

def buscar_codigo(codigo,productos):
    pass

def actualizar_precio(codigo,nuevo_precio,productos):
    pass

def agregar_producto(codigo,nombre,categoria,precio,disponible,stock,vendidos,productos,inventario):
    pass

def eliminar_producto(codigo,productos,inventario):
    pass

def mostrar_productos(productos,inventario):
    pass