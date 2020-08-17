text1 = str(input("ingrese una cadena para invertir: "))

def reverse(cadena):
    if len(cadena) == 1:
        return cadena
    else:
        
     return cadena[-1] + reverse(cadena[:-1])  


text2 = reverse(text1)

if text2 == text1: print(text1, " Es un palíndromo")

else:

    print(text1, " no es un palíndromo")