print("-----------")
print("AUMENTO DE SUELDO DEL 15% AL MENOR DE 1000")
print("-----------")

print("Sueldo")

SUE=float(input("Ingrese sueldo real: "))

if SUE<1000:
    AUM=SUE*0.15
    SUE=SUE+AUM

print("El sueldo total es: ",SUE)