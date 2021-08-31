n=int(input())
a=list(map(int, input().split()))
def selectionsort(n,a):
    cnt=0
    for i in range(n):
        minj=i
        for j in range(i,n):
            if a[minj]>a[j]:
                minj=j
        if a[i]!=a[minj]:
            t=a[i]
            a[i]=a[minj]
            a[minj]=t
            cnt+=1
    print(*a)
    print(cnt)
selectionsort(n,a)