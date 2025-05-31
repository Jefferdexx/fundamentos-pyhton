'''
Clase:        Fase de fortalecimiento lógico
Tema:         Bloques iterativos
Ejercicio:    5.4.1. ¡Adivina el número!
Descripción:  Genera un número aleatorio entre 1 y 100 y pide al usuario que lo adivine.
El programa debe seguir pidiendo números hasta que acierte. En cada
intento fallido el programa notificará al usuario si el número secreto es
mayor o menor al último valor ingresado.

Autor:        Dennys Jefferson Molina Abrego
Fecha:        2025-05-31
Estado:       [Terminado ]
'''
import random

numero_aleatorio = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adivina el número entre 1 y 100: "))
    intentos += 1
    if intento < numero_aleatorio:
        print("El número secreto es mayor.")
    elif intento > numero_aleatorio:
        print("El número secreto es menor.")
    else:
        print(f"¡Felicidades! Has adivinado el número secreto: {numero_aleatorio}")
        break
