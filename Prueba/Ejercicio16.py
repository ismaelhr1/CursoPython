print("-----------")
print("DETERMINA LA SALIDA")
print("-----------")

A=int(input("Ingrese número A: "))
B=int(input("Ingrese número B: "))
C=int(input("Ingrese número C: "))

print("Resultado")

if A>B:
    if A>C:
        if B>C:
            print(A,B,C)
        else:
            print(A,C,B)
    else:
         print(C,A,B)
else:
    if B>C:
        if A>C:
            print(B,A,C)
        else:
            print(B,C,A)
    else:
        print(C,B,A)

