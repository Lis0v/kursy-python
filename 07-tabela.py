wiersz=int(input("Podaj liczbę wierszy: "))
kolumna=int(input("Podaj liczbę kolumn: "))

for i in range(1,wiersz+1):
    print(" ")
    for j in range(1,kolumna+1):
        print(i+j,end=" ")