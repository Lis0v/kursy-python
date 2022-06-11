zm1=int(input("Podaj index elementu ciągu:"))
zm2=int(input("Podaj różnicę pomiędzy wyrazami ciągu:"))
def ciag(n):
    if n==0:
        return 1
    return 2*ciag(n-1)+1
print(ciag(zm1))