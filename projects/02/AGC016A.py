s=input()
print(min(max(map(len,s.split(e))) for e in s))