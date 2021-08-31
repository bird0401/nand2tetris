from math import gcd,sqrt
a,b=map(int,input().split())
g=gcd(a,b)
ans,i=1,2
while i*i<=g:
    if g%i==0:
        ans+=1
        while g%i==0:g//=i
    i+=1
print(ans+(g>1))