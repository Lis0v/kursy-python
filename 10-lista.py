lista1=list(range(0,101,5))
lista2=list(range(-3,10,2))
lista3=[]
lista3.extend(lista1)
lista3.extend(lista2)
for i in lista3:
    print(i,end=" ")
print(" ")
if 5 in lista3:
    print("Wartość 5 jest na liście.")
else:
    print("Wartości 5 nie ma w liście")