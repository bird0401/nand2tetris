from itertools import permutations

s1,s2,s3=(input() for _ in range(3))
ss=s1+' '+s2+' '+s3
l=list(set(s1+s2+s3))
n=len(l)
if n<=10:
    for ns in permutations("0123456789",n):
        sg=ss
        for j in range(n):sg=sg.replace(l[j],ns[j])
        s1,s2,s3=sg.split()
        if int(s1[0])*int(s2[0])*int(s3[0])==0:continue
        if int(s1)+int(s2)==int(s3):
            print(s1,s2,s3,sep='\n')
            exit()
print("UNSOLVABLE")