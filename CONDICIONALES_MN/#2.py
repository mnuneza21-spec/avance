#2.	Pedir dos números y decir si son iguales o no.

import os
os.system("cls") 

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
if num1 == num2:
    print("Los números son iguales.")       
else:    print("Los números son diferentes.")