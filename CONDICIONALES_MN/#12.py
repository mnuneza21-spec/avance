#12	En una llantería se ha establecido una promoción de las llantas marca “Ponchadas”, dicha promoción consiste en lo siguiente:

import os
os.system("cls") 

try:
    cantidad_llantas = int(input("Introduce la cantidad de llantas que deseas comprar: "))
    if cantidad_llantas < 5:
        precio_unitario = 30000
    elif 5 <= cantidad_llantas <= 10:
        precio_unitario = 25000
    else:
        precio_unitario = 20000
    total_a_pagar = precio_unitario * cantidad_llantas
    print(f"El precio por cada llanta es: ${precio_unitario}")
    print(f"El total a pagar por {cantidad_llantas} llantas es: ${total_a_pagar}")
except ValueError:
    print("Error: Por favor, introduce un número entero válido para la cantidad de llantas.")   