# main.py
# Archivo principal que ejecuta el menú del sistema

# main.py
# Archivo principal que ejecuta el menú del sistema

from src import servicios
from src import archivos

# Lista global del inventario
inventario = []

def pedir_precio():
    # Bucle hasta que el usuario ingrese un número válido
    while True:
        try:
            precio = float(input("Precio: "))
            if precio < 0:
                print("No puede ser negativo.")
            else:
                return precio
        except ValueError:
            print("Dato inválido.")

def pedir_cantidad():
    # Bucle hasta que el usuario ingrese un entero válido
    while True:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad < 0:
                print("No puede ser negativa.")
            else:
                return cantidad
        except ValueError:
            print("Dato inválido.")

# Bucle principal del programa
while True:
    print("\nMENU")
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Buscar")
    print("4. Actualizar")
    print("5. Eliminar")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        precio = pedir_precio()
        cantidad = pedir_cantidad()
        servicios.agregar_producto(inventario, nombre, precio, cantidad)

    elif opcion == "2":
        servicios.mostrar_inventario(inventario)

    elif opcion == "3":
        nombre = input("Buscar: ")
        producto_encontrado = servicios.buscar_producto(inventario, nombre)

        if producto_encontrado != None:
            print(f"Nombre: {producto_encontrado['nombre']} | Precio: ${producto_encontrado['precio']} | Cant: {producto_encontrado['cantidad']}")
        else:
            print("No encontrado.")

    elif opcion == "4":
        nombre = input("Nombre a actualizar: ")
        precio = pedir_precio()
        cantidad = pedir_cantidad()

        ok = servicios.actualizar_producto(inventario, nombre, precio, cantidad)

        if ok:
            print("Actualizado.")
        else:
            print("No existe.")

    elif opcion == "5":
        nombre = input("Nombre a eliminar: ")
        ok = servicios.eliminar_producto(inventario, nombre)

        if ok:
            print("Eliminado.")
        else:
            print("No existe.")

    elif opcion == "6":
        datos = servicios.calcular_estadisticas(inventario)

        if datos == None:
            print("No hay datos en el inventario.")
        else:
            # Desempaquetamos la tupla que retorna la función
            total_unidades, valor_total, mas_caro, mayor_stock = datos
            print("Total unidades:", total_unidades)
            print("Valor total: $", valor_total)
            print("Más caro:", mas_caro["nombre"], "($" + str(mas_caro["precio"]) + ")")
            print("Mayor stock:", mayor_stock["nombre"], "(" + str(mayor_stock["cantidad"]) + " unidades)")

    elif opcion == "7":
        ruta = input("Nombre del archivo (ej. datos.csv): ")
        archivos.guardar_csv(inventario, ruta)

    elif opcion == "8":
        ruta = input("Ruta del archivo (ej. datos.csv): ")
        nuevos_datos = archivos.cargar_csv(ruta)

        if len(nuevos_datos) > 0:
            decision = input("¿Reemplazar inventario actual? (s/n): ")

            if decision.lower() == "s":
                inventario.clear() # Limpiamos la lista actual
                inventario.extend(nuevos_datos) # Agregamos los nuevos
                print("Inventario reemplazado.")
            else:
                inventario.extend(nuevos_datos)
                print("Datos fusionados.")
        else:
            print("No se encontraron datos válidos para cargar.")

    elif opcion == "9":
        print("Fin del programa. ¡Adiós!")
        break

    else:
        print("Opción inválida. Intenta de nuevo.")

# Este programa permite gestionar un inventario básico usando listas y diccionarios.
# El usuario puede agregar productos, visualizar el inventario y calcular estadísticas.
# Se aplicaron validaciones de entrada, uso de funciones y estructuras de control
# como bucles y condicionales para asegurar un funcionamiento correcto.
# Este programa permite gestionar un inventario básico usando listas y diccionarios.
# El usuario puede agregar productos, visualizar el inventario y calcular estadísticas.
# Se aplicaron validaciones de entrada, uso de funciones y estructuras de control
# como bucles y condicionales para asegurar un funcionamiento correcto.

