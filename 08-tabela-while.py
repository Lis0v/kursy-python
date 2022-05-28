wiersz=int(input("Podaj liczbę wierszy: "))
kolumna=int(input("Podaj liczbę kolumn: "))

i=1
while i<=wiersz:
    print(" ")
    j=1
    while j<=kolumna:
        print(i+j,end=" ")
        j+=1
    i+=1