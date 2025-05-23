'''
Clase:        Fase de fortalecimiento lógico
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    1.3.1. Automatizando el cálculo de la propina
Descripción:  Pide al usuario el total de una cuenta y el porcentaje de propina
(por ejemplo, 10%, 15%, 20%). Calcula y muestra en pantalla el total
a pagar.

Autor:        Dennys Jefferson Molina Abrego
Fecha:        2025-05-15
Estado:       [Terminado ]
'''

total_cuenta = float(input("Ingrese el total de la cuenta: $"))
propina = float(input("Ingrese el porcentaje de propina: "))
total_pagar = total_cuenta + (total_cuenta * propina / 100)
print(f"\n\nTotal de la cuenta: ${total_cuenta}")
print(f"Propina: ${total_cuenta * propina / 100}")
print(f"Total de la cuenta con propina ({propina}%): ${total_pagar}")