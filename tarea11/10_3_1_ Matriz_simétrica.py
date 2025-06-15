'''
Clase:        Fase de fortalecimiento lógico
Tema:         Manejo de matrices
Ejercicio:    10.3.1. Matriz simétrica
Descripción:  Dada una matriz cuadrada ingresada por el
usuario, comprueba si la matriz cuadrada es
simétrica respecto a su diagonal principal
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

simetrica = True
for i in range(n):
    for j in range(n):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
            break
    if not simetrica:
        break

if simetrica:
    print("\nLa matriz es simétrica.")
else:
    print("\nLa matriz no es simétrica.")
