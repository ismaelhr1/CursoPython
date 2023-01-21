print("--------------")
print("DATOS DEL CILINDRO")
print("--------------")

RADIO=float(input("Introducir RADIO DEL CILINDRO: "))
ALTO=float(input("Introducir ALTO DEL CILINDRO: "))

PI=3.1416

VOL=PI*(RADIO**2)*ALTO
ARE=(2*PI)*RADIO*(ALTO+RADIO)

print("VOLUMEN: ", VOL)
print("AREA: ", ARE)