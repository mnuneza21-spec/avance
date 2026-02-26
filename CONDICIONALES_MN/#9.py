#9.	Pedir una nota numérica entera entre 0 y 10, y mostrar dicha nota de la forma: cero, uno, dos, tres...

import os
os.system("cls") 

nombres_notas = [
    "cero", "uno", "dos", "tres", "cuatro", 
    "cinco", "seis", "siete", "ocho", "nueve", "diez"
]
try:
    nota = int(input("Introduce una nota numérica (0-10): "))


    if 0 <= nota <= 10:
        print(f"La nota es: {nombres_notas[nota]}")
    else:
        print("Error: El número debe estar entre 0 y 10.")
except ValueError:
    print("Error: Por favor, introduce un número entero válido.")