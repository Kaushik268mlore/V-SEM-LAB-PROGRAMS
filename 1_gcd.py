# method 1
def gcd1(a,b):
    res=min(a,b)
    while(res):
        if(a%res==0 and b%res==0):
            break
        res-=1
    return res

#using euler's method
def gcd2(a,b):
    if(a==0):
        return b 
    if(b==0):
        return a
    if(a>b):
        return gcd2(a-b,b)
    return gcd2(a,b-a)

#using memoization on euler's method
dp=[[-1 for i in range(1001)]for j in range(1001)]

def gcd3(a,b):
    if(a==0):
        return b
    if(b==0):
        return a
    if(dp[a][b]!=-1):
        return dp[a][b]
    if(a>b):
        dp[a][b]=gcd3(a-b,b)
    else :
        dp[a][b]=gcd3(a,b-a)
    return dp[a][b]

a=645
b=234
print("GCD1 is :",gcd1(a,b))
print("GCD2 is :",gcd2(a,b))
print("GCD3 is :",gcd3(a,b))
