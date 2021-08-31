n,k=map(int,input().split())
a=list(map(int, input().split()))
s=l=ans=0
for r in range(n):
    s+=a[r]
    while s>=k:
        s-=a[l]
        l+=1
    ans+=l
print(ans)