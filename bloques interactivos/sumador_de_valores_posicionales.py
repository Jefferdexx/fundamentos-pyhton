'''
Clase:        Fase de fortalecimiento lógico
Tema:         Bloques iterativos
Ejercicio:    5.4.2. Sumador de valores posicionales
Descripción:  Pide un número al usuario y suma sus dígitos hasta que quede un solo dígito. Ejemplo:
Si el usuario ingresa 9875, entonces: 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2.

Autor:        Dennys Jefferson Molina Abrego
Fecha:        2025-05-31
Estado:       [Terminado ]
'''

numero = int(input("Ingrese un número: "))
print(f"Proceso de reducción para: {numero}")
while numero >= 10:
    suma  = sum(int(digito) for digito in str(numero))
    print(f"{numero} = {suma}")
    numero = suma
print(f"El resultado final es: {numero}")
    
