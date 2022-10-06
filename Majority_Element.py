d=int(input())
s=list(map(int,input().split()))
c=[]
for i in s:
    c.append(s.count(i))
q=c.index(max(c))
print(s[q])