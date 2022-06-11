przyklad={"klucz1":"wartosc1","klucz2":"wartosc2","klucz3":"wartosc3"}
print(przyklad)
slownik={}
slownik["klucz1"]="wartosc1"
slownik["klucz2"]="wartosc2"
slownik["klucz3"]=59
slownik["klucz4"]=[45,-9,15]
print(slownik)
print(slownik["klucz4"])
slownik["klucz2"]="Ala ma kota"
print(slownik)
slownik["klucz2"]=slownik["klucz2"]+" i psa."
slownik["klucz3"]=slownik["klucz3"]+5
print(slownik)
# slownik.pop("klucz3") # del slownik["klucz3"]
# slownik.clear() - czyszczenie slownika
print(slownik)
print(len(slownik))
print(slownik.items())
print(slownik.keys())
print(slownik.values())
slownik1={"a":50}
print(slownik1)
slownik.update(slownik1)
print(slownik)
miesiac=["Styczeń","Luty","Marzec","Lipiec"]
liczby=[1,2,3,7]
slownik2=dict(zip(miesiac,liczby))
print(slownik2)
print(slownik2["Lipiec"])
print(slownik2.get("Lipiec"))
for i in slownik2:
    print(i)
if ("Lipiec",7) in slownik2.items():
    print("Klucz i wartość istnieje w słowniku.")
else:
    print("Klucza i wartości nie ma w słowniku.")

if 7 in slownik2.values():
    print("Wartość istnieje w słowniku.")
else:
    print("Wartości nie ma w słowniku.")
print(slownik2)
slownik3=slownik2.copy()
slownik4=slownik2
print(slownik3)
print(slownik4)
slownik2.clear()
print(slownik3)
print(slownik4)