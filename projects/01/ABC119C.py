from math import gcd
n,X=map(int,input().split())
ans=0
for e in list(map(int, input().split())):ans=gcd(abs(X-e),ans)
print(ans)