def ciagFib(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return ciagFib(a-1)+ciagFib(a-2)

ile=int(input("Podaj ilość wyrazów ciągu Fibonacciego"))
print(ciagFib(ile))