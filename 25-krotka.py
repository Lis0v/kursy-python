krotka=25,"Dowolny tekst",-89.5
print(krotka)
krotka1=tuple(range(-5,10,2))*4
print(krotka1)
for i in krotka1:
    print(i,end=" ")
print("Krotka o nazwie krotka1 jest",len(krotka1),"elementowa")
print("Odwracamy elementy krotki")
print(krotka1[::-1])
print(krotka1)
print(krotka1[3:6])
krotka2=krotka+krotka1
print(krotka2)