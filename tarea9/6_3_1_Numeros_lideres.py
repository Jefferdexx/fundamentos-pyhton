'''
Clase:        Fase de fortalecimiento lógico
Tema:         Bloques iterativos
Ejercicio:    6.3.1. Números líderes
Descripción:  Un número en una lista es "líder" si es
estrictamente mayor que todos los
elementos a su derecha. Dada una lista de
números ingresada por el usuario, imprime
todos los números líderes.

Autor:        Dennys Jefferson Molina Abrego
Fecha:        2025-06-2
Estado:       [Terminado ]
'''

valores = input("Ingrese una lista de números separados por espacios: ")
valores = valores.split()
valores = list(map(int, valores))
valores.sort()
valores.reverse()
almacenados = []
for elementos in valores:
    if elementos not in almacenados:
        if len(almacenados) < 4:
            almacenados.append(elementos)
print(*almacenados)
