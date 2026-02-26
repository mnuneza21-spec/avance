#	Pedir el día, mes y año de una fecha e indicar si la fecha es correcta. Suponiendo todos los meses de 30 días.

import os
os.system("cls") 

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))
if (dia >= 1 and dia <= 30) and (mes >= 1 and mes <= 12) and (año > 0):
    print("La fecha es correcta.")
else:
    print("La fecha es incorrecta.")    
