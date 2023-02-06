print("-----------")
print("FUNCIÓN")
print("-----------")

print("Ingrese los valores")

NUM=int(input("Tipo de cálculo: "))
V=int(input("Ingrese V: "))

funcion={
    1:100*V,
    2:100**V,
    3:100/V
}

VAL=funcion.get(NUM,0)

print("Resultado: ",VAL)