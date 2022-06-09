x=0
y=1
ile=int(input("Podaj ilość wyrazów ciągu Fibonacciego:"))
print(x,end=" ")
for i in range(0,ile):
    print(y,end=" ")
    y=y+x
    x=y-x