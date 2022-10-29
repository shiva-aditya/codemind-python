def po(a):
    e=0
    o=0
    for i in range(len(a)):
        if i%2!=0:
            o+=sum(a[i])
        else:
            e+=sum(a[i])
    return e,o

f=[]
a,b=map(int,input().split())
for i in range(a):
    d=list(map(int,input().split()))
    f.append(d)
print(*po(f))