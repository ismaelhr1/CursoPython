print("-----------")
print("VERIFICAR SI EL AÑO ES BISIESTO")
print("-----------")

anio=int(input("Introduce el año: "))

if (anio%400==0) or (anio%4==0) and (anio%100!=0):
    print("EL AÑO ES BISIESTO")
else:
    print("EL AÑO NO ES BISIESTO")