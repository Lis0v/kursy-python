liczba1=int(input("Podaj pierwszą liczbę:"))
liczba2=int(input("Podaj drugą liczbę:"))
count=0
if liczba2==0:
    print("NWD to liczba:",liczba1)
else:
    while liczba2>0:
        count=count+1
        reszta=liczba1%liczba2
        liczba1=liczba2
        liczba2=reszta
print("NWD to liczba:",liczba1)
print("Pętla wykonała się",count,"razy.")