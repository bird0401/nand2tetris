n=int(input())
a=list(map(int, input().split()))
def bubblesort(n,a):
    cnt,flag=0,1
    while flag:
        flag=0
        for j in range(n-1,0,-1):
            if a[j-1]>a[j]:
                t=a[j]
                a[j]=a[j-1]
                a[j-1]=t
                cnt+=1
                flag=1
    print(*a)
    print(cnt)
bubblesort(n,a)