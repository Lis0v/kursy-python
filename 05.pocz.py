poczatek=int(input("Podaj początek zakresu: "))
koniec=int(input("Podaj koniec zakresu: "))
suma=0
for i in range(poczatek, koniec+1):
    suma+=i #suma=suma+i
print("Suma liczb z przedziału od",poczatek,"do",koniec,"wynosi",suma)