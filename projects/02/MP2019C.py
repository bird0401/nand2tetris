k,a,b=map(int,input().split())
if b-a<2:print(k+1)
else:print(a+((k-(a-1))//2)*(b-a)+(k-(a-1))%2)