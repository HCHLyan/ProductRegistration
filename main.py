# Lista global donde se almacenan los productos
inventario = []


# ---------------------------
# Función para agregar producto
# ---------------------------
def agregar_producto():
    print("\n--- Agregar producto ---")
    
    # Solicitar nombre
    nombre = input("Ingresa el nombre del producto: ")

    # Validar precio (float)
    while True:
        precio_input = input("Ingresa el precio del producto: ")
        try:
            precio = float(precio_input)
            if precio < 0:
                print("El precio no puede ser negativo.")
                continue
            break
        except ValueError:
            print("Error: ingresa un número válido para el precio.")

    # Validar cantidad (int)
    while True:
        cantidad_input = input("Ingresa la cantidad del producto: ")
        try:
            cantidad = int(cantidad_input)
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue
            break
        except ValueError:
            print("Error: ingresa un número entero válido para la cantidad.")

    # Crear diccionario del producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    # Agregar al inventario
    inventario.append(producto)
    print("Producto agregado correctamente.")


# ---------------------------
# Función para mostrar inventario
# ---------------------------
def mostrar_inventario():
    print("\n--- Inventario ---")

    # Verificar si está vacío
    if len(inventario) == 0:
        print("El inventario está vacío.")
        return

    # Recorrer e imprimir productos
    for producto in inventario:
        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")


# ---------------------------
# Función para calcular estadísticas
# ---------------------------
def calcular_estadisticas():
    print("\n--- Estadísticas ---")

    # Si no hay productos
    if len(inventario) == 0:
        print("No hay productos en el inventario.")
        return

    valor_total = 0
    total_productos = 0

    # Calcular valores
    for producto in inventario:
        valor_total += producto["precio"] * producto["cantidad"]
        total_productos += producto["cantidad"]

    # Mostrar resultados
    print(f"Valor total del inventario: {valor_total}")
    print(f"Cantidad total de productos: {total_productos}")


# ---------------------------
# Menú principal (bucle infinito hasta salir)
# ---------------------------
while True:
    print("\n===== MENÚ =====")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    # Estructura condicional del menú
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        calcular_estadisticas()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intenta nuevamente.")


# ---------------------------
# Resumen final
# ---------------------------
# Este programa permite gestionar un inventario básico usando listas y diccionarios.
# El usuario puede agregar productos, visualizar el inventario y calcular estadísticas.
# Se aplicaron validaciones de entrada, uso de funciones y estructuras de control
# como bucles y condicionales para asegurar un funcionamiento correcto.