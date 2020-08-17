x = int(input("ingrese la base: "))
y = int(input("ingrese el exponente: "))

def potencia(x,y):
    #caso base
    if y == 0:
        return 1
    else:
        po = x*potencia(x,y-1)
        return po

print(potencia(x,y))    