
def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total


if __name__ == "__main__":
    print("=== TIENDA MCS ===")
    print("Productos disponibles:")
    print("1. Pan      - $1.00")
    print("2. Leche    - $1.25")
    print("3. Arroz    - $1.50")
    print("4. Gaseosa  - $1.00")
    print("5. Atún     - $1.75")

    opcion = int(input("Seleccione el número del producto: "))
    cantidad = int(input("Ingrese la cantidad que desea comprar: "))

    if opcion == 1:
        producto = "Pan"
        precio = 1.00
    elif opcion == 2:
        producto = "Leche"
        precio = 1.25
    elif opcion == 3:
        producto = "Arroz"
        precio = 1.50
    elif opcion == 4:
        producto = "Gaseosa"
        precio = 1.00
    elif opcion == 5:
        producto = "Atún"
        precio = 1.75
    else:
        producto = "Producto no válido"
        precio = 0

    if precio > 0:
        resultado = calcular_total(precio, cantidad)

        print()
        print("=== RESUMEN DE COMPRA ===")
        print("Producto:", producto)
        print("Precio unitario: $", precio)
        print("Cantidad:", cantidad)
        print("Total a pagar: $", resultado)
    else:
        print("La opción seleccionada no es válida.")

