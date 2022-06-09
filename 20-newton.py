zm1=int(input("Podaj zmienna n:"))
zm2=int(input("Podaj zmienna k:"))
def newtona(liczba1,liczba2):
    if liczba2 in(0,liczba1):
        return 1
    return newtona(liczba1-1,liczba2-1)+newtona(liczba1-1,liczba2)
print(newtona(zm1,zm2))
