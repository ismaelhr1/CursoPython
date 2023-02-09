print("-----------")
print("COMPRA CON DESCUENTO")
print("-----------")

costo=float(input("Ingrese el coste del artículo: "))
m=input("Ingrese la marca: ")


if costo>=2000 and m=="NOSY":
    pa=costo*0.90
    pt=costo*0.95

elif costo>=2000 and m!="NOSY":
    pt=costo*0.90

elif costo<2000 and m=="NOSY":
    pa=costo*0.95
    pt=pa+pa*0.20

elif costo<2000 and m!="NOSY":
    pt=costo*1.20

print("Usted pagara: ",pt, "soles")

