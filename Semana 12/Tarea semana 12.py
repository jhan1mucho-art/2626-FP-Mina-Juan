# Programa para reservar un asiento en una sala de cine
# La sala tiene 3 filas y 4 columnas.
# 0 = asiento libre
# 1 = asiento reservado

# Crear la matriz de 3 filas por 4 columnas,
# inicializando todos los asientos como libres (0).
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Solicitar al usuario la fila y la columna del asiento.
fila = int(input("Ingrese la fila del asiento (0 a 2): "))
columna = int(input("Ingrese la columna del asiento (0 a 3): "))

# Reservar el asiento seleccionado.
asientos[fila][columna] = 1

# Mostrar el estado de la sala.
print("\nEstado de la sala:")

# Recorrer las filas y columnas utilizando bucles anidados.
for fila in range(len(asientos)):
    for columna in range(len(asientos[fila])):
        print(asientos[fila][columna], end=" ")
    print()
    