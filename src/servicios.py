# servicios.py

# Agrega un producto al inventario
def agregar_producto(inventario, nombre, precio, cantidad):
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)


# Muestra los productos
def mostrar_inventario(inventario):
    if inventario == []:
        print("No hay productos.")
    else:
        for p in inventario:
            print("Producto:", p["nombre"], "| Precio:", p["precio"], "| Cantidad:", p["cantidad"])


# Buscar producto por nombre
def buscar_producto(inventario, nombre):
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None


# Actualizar producto
def actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad):
    producto = buscar_producto(inventario, nombre)

    if producto != None:
        producto["precio"] = nuevo_precio
        producto["cantidad"] = nueva_cantidad
        return True
    else:
        return False


# Eliminar producto
def eliminar_producto(inventario, nombre):
    producto = buscar_producto(inventario, nombre)

    if producto != None:
        inventario.remove(producto)
        return True
    else:
        return False


# Calcular estadísticas
def calcular_estadisticas(inventario):
    if inventario == []:
        return None

    total_unidades = 0
    valor_total = 0

    mas_caro = inventario[0]
    mayor_stock = inventario[0]

    for p in inventario:
        total_unidades = total_unidades + p["cantidad"]
        valor_total = valor_total + (p["precio"] * p["cantidad"])

        if p["precio"] > mas_caro["precio"]:
            mas_caro = p

        if p["cantidad"] > mayor_stock["cantidad"]:
            mayor_stock = p

    return total_unidades, valor_total, mas_caro, mayor_stock