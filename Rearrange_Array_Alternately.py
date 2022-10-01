def po(a,l):
    g=[]
    while a:
        if len(a)==1:
            g.append(a[0])
            break
        else:
            g.append(max(a))
            g.append(min(a))
            a.remove(max(a))
            a.remove(min(a))
    return g
    
for _ in  range(int(input())):
    f=int(input())
    g=list(map(int,input().split()))
    print(*po(g,f))