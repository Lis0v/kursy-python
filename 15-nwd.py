liczba1=int(input("Podaj pierwszą liczbę:"))
liczba2=int(input("Podaj drugą liczbę:"))
zm1=liczba1
zm2=liczba2
count=0
while liczba1!=liczba2: #!=różne
    count+=1 #count=count+1
    if liczba1>liczba2:
        liczba1=liczba1-liczba2
    else:
        liczba2=liczba2-liczba1
print("NWD liczb",zm1,"oraz",zm2,"wynosi",liczba1)
print("Pętla wykonała się",count,"razy.")