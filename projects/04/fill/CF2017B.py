s=input()
b=[s.count('a'),s.count('b'),s.count('c')]
print("YES" if max(b)-min(b)<2 else "NO")