
# ==========================================
# SISTEMA DE REGISTRO DE PRODUCTOS
# Tarea Semana 15
# Funciones, Colecciones y Archivos
# ==========================================

# Diccionario donde se almacenarán los productos.
# La clave será el nombre del producto
# y el valor será su precio.
productos = {}


# ------------------------------------------
# FUNCIÓN PARA AGREGAR UN PRODUCTO
# ------------------------------------------
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")

    # Verificamos que el producto no exista.
    if nombre in productos:
        print("El producto ya se encuentra registrado.")
    else:
        precio = float(input("Ingrese el precio del producto: "))
        productos[nombre] = precio
        print("Producto agregado correctamente.")


# ------------------------------------------
# FUNCIÓN PARA MOSTRAR LOS PRODUCTOS
# ------------------------------------------
def mostrar_productos():
    if len(productos) == 0:
        print("No existen productos registrados.")
    else:
        print("\n===== PRODUCTOS REGISTRADOS =====")

        for nombre, precio in productos.items():
            print(f"Producto: {nombre} | Precio: ${precio:.2f}")


# ------------------------------------------
# FUNCIÓN PARA BUSCAR UN PRODUCTO
# ------------------------------------------
def buscar_producto():
    nombre = input("Ingrese el nombre del producto que desea buscar: ")

    if nombre in productos:
        print(f"Producto encontrado: {nombre}")
        print(f"Precio: ${productos[nombre]:.2f}")
    else:
        print("El producto no se encuentra registrado.")


# ------------------------------------------
# FUNCIÓN PARA ELIMINAR UN PRODUCTO
# ------------------------------------------
def eliminar_producto():
    nombre = input("Ingrese el nombre del producto que desea eliminar: ")

    if nombre in productos:
        del productos[nombre]
        print("Producto eliminado correctamente.")
    else:
        print("El producto no existe.")


# ------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------

while True:

    print("\n================================")
    print("   SISTEMA DE PRODUCTOS")
    print("================================")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()

    elif opcion == "2":
        mostrar_productos()

    elif opcion == "3":
        buscar_producto()

    elif opcion == "4":
        eliminar_producto()

    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")

