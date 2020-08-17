cadena = str(input("ingrese una cadena para invertir: "))

def reverse(cadena):
    if len(cadena) == 1:
        return cadena
    else:
        
     return cadena[-1] + reverse(cadena[:-1])   

print(reverse(cadena))