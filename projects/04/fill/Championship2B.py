n=int(input())
d=list(map(int, input().split()))
dp=[0]*n
for e in d:dp[e]+=1
ans=1 if dp[0]==1 and d[0]==0 else 0
for i in range(1,n):ans*=dp[i-1]**dp[i]
print(ans%998244353)