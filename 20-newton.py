zm1=int(input("Podaj liczbe wszystkich kul:"))
zm2=int(input("Podaj ilosc kul, ktore losujemy:"))
def newtona(liczba1,liczba2):
    if liczba2 in(0,liczba1):
        return 1
    return newtona(liczba1-1,liczba2-1)+newtona(liczba1-1,liczba2)
print("Prawdopodobienstwo wylosowania",zm2,"liczb sposrod",zm1,"wynosi",newtona(zm1,zm2))