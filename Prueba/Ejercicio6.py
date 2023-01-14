print("----------------")
print("DISTANCIA COORDENADAS")
print("----------------")

print("Ingresa coordenadas del punto A")
AX=float(input("Introduce coordenada AX: "))
AY=float(input("Introduce coordenada AY: "))

print("Ingresa coordenadas del punto B")
BX=float(input("Introduce coordenada BX: "))
BY=float(input("Introduce coordenada BY: "))

D=((AX-BX)**2 + (AY-BY)**2)**0.5

print("Resultado: ",D)

