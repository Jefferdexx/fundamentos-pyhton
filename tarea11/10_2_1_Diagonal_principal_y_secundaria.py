'''
Clase:        Fase de fortalecimiento lógico
Tema:         Manejo de matrices
Ejercicio:    10.2.1. Diagonal principal y secundaria
Descripción:  Dada una matriz cuadrada ingresada por el
usuario, crea dos listas, una con los
elementos de la diagonal principal y la otra
con los elementos de la diagonal
secundaria
Autor:        Dennys Jefferson Molina Abrego
Fecha:        2025-06-14
Estado:       [Terminado ]
'''

n = int(input("Ingrese la dimensión de la matriz: "))

matriz = []
for i in range(n):
    fila = list(map(int, input(f"Ingrese fila {i + 1} separados por comas (1,2,3...): ").split(",")))
    matriz.append(fila)
    if len(fila) != n:
        print(f"La fila debe tener la misma cantidad de elementos que la dimensión ingresada. \n")
        exit()

diagonal_principal = []
diagonal_secundaria = []

for i in range(n):
    diagonal_principal.append(matriz[i][i])
    diagonal_secundaria.append(matriz[i][n - 1 - i])
    
print(diagonal_principal)
print(diagonal_secundaria)