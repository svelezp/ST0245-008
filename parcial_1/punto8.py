numero = int(input("Ingrese los dos ultimos números de su tarjeta de identidad: "))
def invert(n):
    if n > 1:
        print(n)
        invert(n-1)
    else:
        print(1)

      


print(invert(numero))
