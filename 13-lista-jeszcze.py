

lista=[]
for i in range(15,30):
    if not (i % 3):
        lista.append(i)
print(lista)

lista2=list(range(15,30,3))
print(lista2)