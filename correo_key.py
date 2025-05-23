'''
Clase:        Fase de fortalecimiento lógico
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    1.3.2. Generador del correo de Key
Descripción:  Solicita al usuario su nombre completo (asume dos nombres y dos apellidos). Luego, el programa generará, su correo.
Autor:        Dennys Jefferson Molina Abrego
Fecha:        2025-05-15
Estado:       [Terminado ]
'''


nombre = input("Ingrese su nombre completo: ")
nombre = nombre.lower()
correo = nombre.split()
primer_nombre = correo[0]
primer_apellido = correo[2]
print(f"\nEl correo que se debe asignar al usuario ingresado es: \n{primer_nombre}.{primer_apellido}@keyinstitute.edu.sv")