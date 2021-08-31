import sys
sys.setrecursionlimit(10**9)

n=int(input())
c=list(map(int, input().split()))
graph=[[] for _ in range(n)]x
for i in range(n-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    graph[a]+=[b]
    graph[b]+=[a]
ans=[]
co=[0]*((10**5)+1)
def dfs(now,pre):
    global ans
    if co[c[now]]==0:ans+=[now+1]
    co[c[now]]+=1
    for to in graph[now]:
        if to!=pre:dfs(to,now)
    co[c[now]]-=1
dfs(0,-1)
ans.sort()
print(*ans,sep='\n')