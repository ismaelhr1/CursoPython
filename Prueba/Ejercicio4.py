print("---------------")
print("PUNTUACIÓN PARTIDOS")
print("---------------")

PG=int(input("Ingresar número de partidos ganados: "))
PE=int(input("Ingresar número de partidos empatados: "))
PP=int(input("Ingresar número de partidos perdidos: "))

PPG=PG*3
PPE=PE*1
PPP=PP*0

PF=PPG+PPE+PPP

print("Puntos: ",PF)
