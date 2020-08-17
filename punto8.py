import sys

def pos(colum,fila):
    if(colum==0) or (fila == colum):
        return 1
    else:
        return pos(colum-1,fila-1) + pos(colum,fila-1)

def Pascal(num):

    for f in range(num):
        for c in range(f+1):
            sys.stdout.write(str(pos(c,f))+" ")
        print('\n')
num=int(input("Ingrese el numero de filas del triangulo: "))
print(Pascal(num+1))