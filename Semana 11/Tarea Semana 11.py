
# =========================================================
# Tarea Semana 11
# Asignatura: Fundamentos de Programación
# Tema: Arreglos Multidimensionales (Matriz 5x5)
# Autor: Juan Mina
# =========================================================

# Inicialización de una matriz de 5x5 con ceros
matriz = [[0 for _ in range(5)] for _ in range(5)]

print("=== INGRESO DE DATOS A LA MATRIZ (5x5) ===")

# Bucles anidados para solicitar y almacenar los 25 valores desde la consola
for i in range(5):
    for j in range(5):
        valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
        matriz[i][j] = valor

print("\n=== MATRIZ INGRESADA ===")

# Bucles anidados para recorrer y mostrar el contenido en formato de tabla
for i in range(5):
    for j in range(5):
        print(matriz[i][j], end="\t")
    print()