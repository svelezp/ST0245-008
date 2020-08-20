import sys

def  pascal(row, column):
          if row < 0 and column < 0:
                return 0
          elif(row == 0) or (column == 0):
                return 1
          else:
                return(pascal(column-1, row-1)) + (pascal(column, row-1))

def Pascal2(num):

    for f in range(num):
        for c in range(f+1):
            sys.stdout.write(str(pascal(c,f))+" ")
        print('\n')
num=int(input("Ingrese el numero de filas del triangulo: "))
print(Pascal2(num+1))
            