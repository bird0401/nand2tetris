s=input()
ans=0
n=len(s)
for i in range(n):
    if s[i]=='U':ans+=(n-i-1)+2*i
    else:ans+=2*(n-i-1)+i
print(ans)