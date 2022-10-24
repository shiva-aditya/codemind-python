def po(a):
    if len(a)%2!=0:
        e=len(a)//2
        a.insert(e+1,0)
    c=[]
    for i in range(0,len(a)//2):
        c.append(a[i])
        c.append(a[len(a)-i-1])
    return c
    
s=int(input())
q=list(map(int,input().split()))
print(*po(q))