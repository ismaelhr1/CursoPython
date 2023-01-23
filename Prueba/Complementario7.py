import math

print("-----------")
print("TERCER LADO DE UN TRIÁNGULO")
print("-----------")

PI=3.1416

B=float(input("Ingrese lado B: "))
C=float(input("Ingrese lado c: "))

ALFA=float(input("Ingrese el ángulo en grados sexadecimales: "))

A=(B**2+C**2-2*B*C*math.cos(ALFA*PI/180))**0.5

print("El lado A del triángulo es:",A)

