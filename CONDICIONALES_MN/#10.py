#	Diseñe un algoritmo que lea un número de tres cifras y determine si es o no capicúa. Un número es capicúa si es igual al derecho y al revés del número.

import os
os.system("cls") 

try:
    compra = float(input("Introduce el monto de tu compra: "))

    if compra > 300000:
        descuento = compra * 0.20
        total_a_pagar = compra - descuento
        print(f"¡Felicidades! Has obtenido un descuento del 20% (${descuento:,.0f}).")
        print(f"Total a pagar: ${total_a_pagar:,.0f}")
    else:
        print(f"No se aplica descuento. Total a pagar: ${compra:,.0f}")
except ValueError:
    print("Error: Por favor, introduce un monto válido sin puntos ni comas.")
