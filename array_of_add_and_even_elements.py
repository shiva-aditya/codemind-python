def po(a):
    c=[]
    e=[]
    for i in a:
        if i%2!=0:
            c.append(i)
        else:
            e.append(i)
    c.extend(e)
    return c
        
    
    
s=int(input())
p=list(map(int,input().split()))
print(*po(p))