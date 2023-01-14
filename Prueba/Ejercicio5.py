import math

print("---------")
print("NÚMERO DE MICRODISCOS NECESARIOS DE 3,5")
print("---------")

GB=float(input("Ingrese GB: "))

MG=GB*1024
MD=MG/1.44

print(MD)
print("Se necesitan ", math.ceil(MD)," microdiscos")