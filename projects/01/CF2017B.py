from collections import Counter
n=int(input())
d=Counter(list(map(int, input().split())))
m=int(input())
t=Counter(list(map(int, input().split())))
print("NO" if t-d else "YES")