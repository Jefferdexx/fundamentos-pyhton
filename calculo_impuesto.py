'''
Clase:        Fase de fortalecimiento lógico
Tema:         Bloque condicional
Ejercicio:    2.3.2. Cálculo de impuesto
Descripción:  Desarrollar un programa en Python que permita calcular el impuesto que debe pagar
un usuario por el consumo de energía.

Autor:        Dennys Jefferson Molina Abrego
Fecha:        2025-05-15
Estado:       [Terminado ]
'''


print("Bienvenido al programa de cálculo de impuestos por consumo de energía\n")
unidades = int(input("Ingrese las unidades consumidas de energía en números enteros: "))
if unidades <= 100:
    print("Sin impuestos")
elif unidades <= 200:
    impuesto = unidades * 0.5
    print(f"El impuesto aplicado es de ${impuesto}")
else:
    impuesto = unidades * 0.7
    print(f"El impuesto aplicado es de ${impuesto}")