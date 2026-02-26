
#7.	Pedir el día, mes y año de una fecha e indicar si la fecha es correcta. Con meses de 28, 30 y 31 días. Sin años bisiestos.

import os
os.system("cls") 

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))
if (mes >= 1 and mes <= 12) and (año > 0):
    if (mes == 2 and dia >= 1 and dia <= 28) or (mes in [4, 6, 9, 11] and dia >= 1 and dia <= 30) or (mes in [1, 3, 5, 7, 8, 10, 12] and dia >= 1 and dia <= 31):
        print("La fecha es correcta.")
    else:
        print("La fecha es incorrecta.")
else:
    print("La fecha es incorrecta.")