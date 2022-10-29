def po(a):
    e=0
    o=0
    for i in a:
        for j in i:
            if j%2==0:
                e+=j
            else:
                o+=j
    return e,o






e=[]
a,b=map(int,input().split())
for i in range(a):
    d=list(map(int,input().split()))
    e.append(d)
print(*po(e))