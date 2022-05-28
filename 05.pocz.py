poczatek=int(input("Podaj początek zakresu: "))
koniec=int(input("Podaj koniec zakresu: "))
krok=int(input("Podaj wartość kroku: "))
suma=0
for i in range(poczatek,koniec+1,krok):
    suma+=i #suma=suma+i
print("Suma liczb z przedziału od",poczatek,"do",koniec,"(krok =",krok,") wynosi",suma)

'''
poczatek=5
koniec=10
i=poczatek  i=5
czy i<koniec+1  5<11 TAK
suma=suma+i     suma=0+5=5
i=6
czy 6<11 TAK suma=5+6=11
'''