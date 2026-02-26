#	Diseñe un algoritmo que lea un número de tres cifras y determine si es o no capicúa. Un número es capicúa si es igual al derecho y al revés del número.

import os
os.system("cls") 

try:
    numero = int(input("Introduce un número de tres cifras: "))
    
    if 100 <= numero <= 999:
        # Extraer el primer y último dígito
        centenas = numero // 100
        unidades = numero % 10
        
        if centenas == unidades:
            print(f"El número {numero} es capicúa.")
        else:
            print(f"El número {numero} no es capicúa.")
    else:
        print("Error: El número debe tener exactamente tres cifras.")
except ValueError:
    print("Error: Debes ingresar un número entero.")
