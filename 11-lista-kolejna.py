lista1=list(range(0,15))
lista2=list(range(-10,10,2))
lista3=lista1+lista2
print(lista3)
lista1.append("Piotrek")
print(lista1)
lista1.insert(2,"Janek")
print(lista1)
del lista1[2]
lista1.pop()
print(lista1)
print(lista3)
while "Janek" in lista3:
    lista3.remove("Janek")
    print(lista3)
    lista.clear()
    print(lista1)
lista4=list(range(0,20))
lista5=lista4.copy()
lista5.append("Wojtek")
lista6=lista4
print("********************")
print(lista4)
print(lista5)
print(lista6)
lista6.reverse();
print(lista6)
lista5=list(range(20,-20,-2))
print(lista5)
lista5.sort()
print(lista5)
print(lista6.count("Ania"))
print(min(lista5))
print(max(lista5))
print(sum(lista5))