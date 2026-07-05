productos = {
    "P101": ["Cuaderno", "Papelería", 2490, True],
    "P102": ["Lápiz", "Papelería", 590, True],
    "P103": ["Botella", "Accesorios", 6990, False],
    "P104": ["Mochila", "Accesorios", 24990, True]
}

inventario = {
    "P101": [30, 15],
    "P102": [120, 50],
    "P103": [0, 10],
    "P104": [8, 25]
}

def mostrar_menu():
    print('''========== MENÚ PRINCIPAL ==========
    1. Stock por categoría
    2. Buscar productos por rango de precio
    3. Actualizar precio 4. Agregar producto
    5. Eliminar producto
    6. Mostrar productos
    7. Salir
    ===================================''')

while True:
    mostrar_menu()