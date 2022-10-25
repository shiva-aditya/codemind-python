def po(a,l):
    c=[]
    for i in range(0,l,2):
        for j in range(a[i+1]):
            c.append(a[i])
    return c

s=int(input())
q=list(map(int,input().split()))
print(*po(q,s))