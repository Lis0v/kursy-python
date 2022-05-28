imie="Piotr"
nazwisko="Nowak"
imie_i_nazwisko="Imie i nazwisko: "
imie_i_nazwisko+="Piotr"+" "+"Nowak"
print(imie_i_nazwisko)
print("Ilość liter w imieniu",imie,"to:",len(imie))

tekst="Jakiś przykładowy tekst"[::-1]
print(tekst)

spr=input("Podaj wyraz - sprawdzimy czy jest palindromem: ")
if spr==spr[::-1]:
    print("Wyraz jest palindromem")
else:
    print("Wyraz nie jest palindromem")

print(tekst.upper())
print(tekst.lower())