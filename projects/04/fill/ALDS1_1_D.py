inf=10**20

n=int(input())
r=[int(input()) for _ in range(n)]
mir,ans=r[0],-inf
for i in range(1,n):
    ans=max(ans,r[i]-mir)
    mir=min(mir,r[i])
print(ans)