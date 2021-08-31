n=int(input())
a,s=10,0
if(n%2==0):
    while a<=n:
        s+=n//a
        a*=5
print(s)