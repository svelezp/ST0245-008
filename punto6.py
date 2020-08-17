n = int(input("digite el numero de iteraciones: "))
def fib_recurs(n):
    if n <= 2:
        return 1
    else:
        return fib_recurs(n - 1) + fib_recurs(n - 2)

print( " El valor para la sucesión", n, fib_recurs(n))