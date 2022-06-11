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