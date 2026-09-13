# =========================================================
# Asignatura: Fundamentos de Programación
# Tema: Arreglos Multidimensionales (Matriz 3x3)
# Autor: [Juan Mina]
# =========================================================

def main():
    # Declarar una matriz 3x3 de enteros
    matriz = [
        [2, 4, 6],
        [1, 3, 5],
        [7, 8, 9]
    ]

    # Recorrer la matriz con ciclos anidados e imprimir todos los valores
    for i in range(3):
        for j in range(3):
            print(f"matriz[{i}][{j}] = {matriz[i][j]}")

    print("-" * 20)
    print("\nMatriz completa:")

    for fila in matriz:
        print(fila)

if __name__ == "__main__":
    main()
