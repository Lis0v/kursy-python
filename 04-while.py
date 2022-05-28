liczba=int(input("Podaj liczbę, której silnię chcesz obliczyć: "))
silnia=1
i=1
while i<=liczba:
    silnia*=i #silnia=silnia*1
    i+=1 #i=i+1
print("Silnia liczby",liczba,"wynosi",silnia,".")