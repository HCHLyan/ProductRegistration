# Solicitar el nombre del producto al usuario
nombre = input("Ingresa el nombre del producto: ")

# Solicitar el precio del producto y validar que sea un número decimal
while True:
    precio_input = input("Ingresa el precio del producto: ")
    try:
        precio = float(precio_input)  # Convertir a tipo float
        break  # Si la conversión funciona, salir del ciclo
    except ValueError:
        print("Error: ingresa un número válido para el precio.")

# Solicitar la cantidad del producto y validar que sea un número entero
while True:
    cantidad_input = input("Ingresa la cantidad del producto: ")
    try:
        cantidad = int(cantidad_input)  # Convertir a tipo int
        break  # Si la conversión funciona, salir del ciclo
    except ValueError:
        print("Error: ingresa un número entero válido para la cantidad.")