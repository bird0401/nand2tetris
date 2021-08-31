n,m=map(int,input().split())
print(m//2 if m-2*n<0 else n+(m-2*n)//4)