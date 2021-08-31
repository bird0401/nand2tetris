n,m=map(int,input().split())
x=list(map(int, input().split()))
x.sort()
d=[x[i]-x[i-1] for i in range(1,m)]
d.sort(reverse=True)
print(sum(d[n-1:]))