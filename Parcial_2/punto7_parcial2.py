pilaA=[]
pilaB=[]


pilaA.append(10)
pilaA.append(20)
pilaA.append(30)
pilaA.append(40)
pilaA.append(50)

print(pilaA)

while(len(pilaA)!=0):
    pilaB.append(pilaA.pop())

print(pilaB)
print(pilaA)