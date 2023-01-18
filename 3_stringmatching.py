def match(a,b):
    m=len(a)
    n=len(b)
    for i in range(n-m+1):
        j=0
        while(j<m):
            if(a[j]!=b[i+j]):
                break
            j+=1
        if(j==m):
            print("String found at ",i)

a="asdfghjkl"
b="ghj"
match(b,a)