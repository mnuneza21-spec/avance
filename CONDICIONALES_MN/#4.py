#4	Pedir dos números y decir cuál es el mayor o si son iguales

import os
os.system("cls") 

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))


if num1 > num2:
    print(f"El mayor es {num1}")
elif num2 > num1:
    print(f"El mayor es {num2}")
else:
    print("Ambos números son iguales")
