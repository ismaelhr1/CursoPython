print("-------------")
print("PUNTUACIÓN FINAL")
print("-------------")

print("Ingrese la puntuación")
RC=int(input("Ingrese número de respuestas correctas: "))
RI=int(input("Ingrese número de respuestas incorrectas: "))
RB=int(input("Ingrese número de respuestas en blanco: "))

PRC=RC*3
PRI=RI*-1
PRB=RB*0
PF=PRC+PRI+PRB

print("Puntuación final: ",PF)
