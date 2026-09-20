# Programa para calcular el precio total de una compra
# 1. Definir la función

def calcular_total(precio, cantidad):
    """
    Calcula el precio total de una compra.

    :param precio: Precio unitario del producto
    :param cantidad: Cantidad de productos comprados
    :return: Precio total de la compra
    """
    total = precio * cantidad
    return total
# 2. Solicitar al usuario los datos de entrada
# Datos de entrada
print("---------------------------------------------")
producto = input("Ingrese el nombre del producto: ")
print("---------------------------------------------")
precio = float(input("Ingrese el precio unitario del producto: "))
print("---------------------------------------------")
cantidad = int(input("Ingrese la cantidad de productos comprados: "))
print("---------------------------------------------")

# Cálculo del precio total
# Llamada a la funcion

total = calcular_total(precio, cantidad)

# Mostrar el resultado

print("\n--- RESUMEN DE LA COMPRA ---")
print(f"Producto: {producto}")
print(f"Precio unitario: {precio}")
print(f"Cantidad: {cantidad}")
print("---------------------------------------------")
print("---------------------------------------------")
print(f"El precio total de la compra es: {total}")
print("---------------------------------------------")
