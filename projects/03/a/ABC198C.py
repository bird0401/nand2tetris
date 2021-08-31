from math import sqrt,ceil
r,x,y=map(int,input().split())
d=sqrt(x**2+y**2)
print(2 if d<r else int(ceil(d/r)))