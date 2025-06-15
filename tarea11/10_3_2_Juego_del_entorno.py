'''
Clase:        Fase de fortalecimiento lógico
Tema:         Manejo de matrices
Ejercicio:    10.3.2. Juego del entorno
Descripción:  Dada una matriz binaria ingresada por el
usuario, verifica para cada celda de una
matriz binaria cuántos elementos con valor
de 1 hay en las celdas vecinas (arriba, abajo,
izquierda, derecha, diagonales).
Autor:        Dennys Jefferson Molina Abrego
Fecha:        2025-06-14
Estado:       [Terminado ]
'''

n = int(input("Ingrese la dimensión de la fila de la matriz: "))
m = int(input("Ingrese la dimensión de la columna de la matriz: "))

matriz = []

for i in range(n):
    fila = list(map(int, input(f"Ingrese fila {i + 1} separados por comas (1,2,3...): ").split(",")))
    matriz.append(fila)
    if len(fila) != m:
        print(f"La fila debe tener la misma cantidad de elementos que la dimensión ingresada. \n")
        exit()

def vecinos(matriz, i, j):
    total = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if (x >= 0 and x < n) and (y >= 0 and y < m) and (x != i or y != j):
                total += matriz[x][y]
    return total
resultado = []
for i in range(n):
    fila_resultado = []
    for j in range(m):
        fila_resultado.append(vecinos(matriz, i, j))
    resultado.append(fila_resultado)

for fila in resultado:
    print(fila)
    