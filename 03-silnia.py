liczba=int(input("Podaj liczbę, której silnię chcesz obliczyć: "))
silnia=1
for i in range(1,liczba+1):
    silnia*=i #silnia=silnia*i
print("Silnia liczby",liczba,"wynosi",silnia,".")