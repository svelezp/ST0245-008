n = int(input("Ingrese el número mayor: "))
m = int(input("Ingrese el número menor: "))
def mcd (n, m):
    if m == 0: return n
     
    return mcd(m, n%m)

print("El maximo común divisor de: ", n, "y: ", m, "es: ", mcd(n, m))
