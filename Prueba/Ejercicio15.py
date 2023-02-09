print("-----------")
print("PAR O IMPAR")
print("-----------")

print("Ingrese un número")

NUM=int(input("Número: "))

numero={
    0:"PAR",
    1:"IMPAR",
    2:"PAR",
    3:"IMPAR",
    4:"PAR",
    5:"IMPAR",
    6:"PAR",
    7:"IMPAR",
    8:"PAR",
    9:"IMPAR",
    10:"PAR"
}

RESULTADO=numero.get(NUM, "NO VÁLIDO")

print("El número es: ",RESULTADO)

