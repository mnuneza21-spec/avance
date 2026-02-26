#1.	Pedir un número e indicar si es positivo o negativo.

import os
os.system("cls")  

num = float(input("Ingrese un número: "))
if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")