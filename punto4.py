palabra = input("Ingrese la palabra: ")
def imp(palabra, n):
    if n < len(palabra):
        print(palabra[0:n])
        imp(palabra, n+1)
    else:
        print(palabra)

print(imp(palabra, 0))