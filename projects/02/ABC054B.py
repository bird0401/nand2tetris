n,m=map(int,input().split())
a=[list(input()) for _ in range(n)]
b=[list(input()) for _ in range(m)]
print("Yes" if any([e[j:j+m] for e in a[i:i+m]]==b for j in range(n-m+1) for i in range(n-m+1)) else "No")