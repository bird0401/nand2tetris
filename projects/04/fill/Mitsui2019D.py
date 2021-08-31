n=int(input())
s=input()
ans=0
for i in range(0,1000):
    si,j=str(i).zfill(3),0
    for e in s:
        if si[j]==e:j+=1
        if j==3:
            ans+=1
            break
print(ans)