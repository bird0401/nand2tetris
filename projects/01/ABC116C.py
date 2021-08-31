n=int(input())
h=list(map(int, input().split()))
ans=0
while True:
    l=0
    while l<n and h[l]==0:l+=1
    if l==n:break
    r=l
    while r<n and h[r]!=0:r+=1
    hm=min(h[l:r])
    ans+=hm
    for i in range(l,r):
        h[i]-=hm
print(ans)