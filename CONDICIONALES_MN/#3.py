#3.	Pedir dos números y decir si uno es múltiplo del otro.

import os
os.system("cls") 

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))          
if num1 % num2 == 0:
    print(f"{num1} es múltiplo de {num2}.") 
elif num2 % num1 == 0:
    print(f"{num2} es múltiplo de {num1}.") 
else:
    print("Los números no son múltiplos entre sí.")