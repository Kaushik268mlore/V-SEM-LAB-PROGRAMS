def sieve(n):
    primes=[True for i in range(n+1)]
    p=2
    while(p*p<=n):
        if(primes[p]==True):
            for i in range(p*p,n+1,p):
                primes[i]=False
        p+=1
    for p in range(2,n+1):
        if primes[p]:
            print(p)

a=10
print("following are the prime numbers less than a:")
sieve(a)