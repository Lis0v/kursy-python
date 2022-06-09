import math
zm1=int(input("Podaj zm1:"))
zm2=int(input("Podaj zm2:"))
print("1-dodawanie")
print("2-odejmowanie")
print("3-mnożenie")
print("4-dzielenie")
print("5-potęga")
print("6-pierwiastek")
flaga=int(input("Wybierz działanie:"))
def odejmowanie(a,b):
    return(print("Różnica wynosi",a-b))
def potega(a,b):
    return(print("Liczba",a,"do potęgi",b,"wynosi",a**b))
def pierwiastek(a,b):
    return(print("Pierwiastek",b,"z liczby",a,"wynosi",a**(1/b)))

if flaga==2:
    odejmowanie(zm1,zm2)
elif flaga==5:
    potega(zm1,zm2)
elif flaga==6:
    pierwiastek(zm1,zm2)
else:
    print("Nie wybrałeś odpowiedniego działania!")