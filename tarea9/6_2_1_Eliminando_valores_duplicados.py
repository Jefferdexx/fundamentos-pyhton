'''
Clase:        Fase de fortalecimiento lógico
Tema:         Bloques iterativos
Ejercicio:    6.2.1. Eliminando valores duplicados
Descripción:  Dada una lista ingresada por el usuario,
elimina los elementos duplicados
manteniendo la primera aparición de cada
número.

Autor:        Dennys Jefferson Molina Abrego
Fecha:        2025-06-2
Estado:       [Terminado ]
'''
valores = input("Ingrese una lista de números separados por espacios: ")
valores = valores.split() 
almacenados = []
for elementos in valores:
    if elementos not in almacenados:
        almacenados.append(elementos)
print(*almacenados)

