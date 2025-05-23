'''
Clase:        Fase de fortalecimiento lógico
Tema:         Bloque condicional
Ejercicio:    2.3.1. Contraseña segura
Descripción:  Solicita una cadena de texto que representa una contraseña, y verifica si la contraseña
cumple con las siguientes condiciones: tener al menos 8 caracteres, un número y una
mayúscula.

Autor:        Dennys Jefferson Molina Abrego
Fecha:        2025-05-15
Estado:       [Terminado ]
'''

contra = input("Dame una contraseña: ")
verif1 = len(contra) >= 8
verif2 = False
for i in contra:
    if i.isdigit():
        verif2 = True
        break
    else:
        verif2 = False
verif3 = False
for i in contra:
    if i.isupper():
        verif3= True
        break
    else:
        verif3 = False

if verif1 and verif2 and verif3:
    print("Contraseña es segura")
else:
    print("Contraseña no segura")