s=int(input())
p=list(map(int,input().split()))
c=[]
e=[]
for i in p:
    if i%2==0:
        c.append(i)
    else:
        e.append(i)
c.extend(e)
print(*c)