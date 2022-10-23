def po(a,l):
    s=sum(a)
    d=s//l
    c=0
    for i in a:
        if i>=d:
            c+=1
    return c
            
    
s=int(input())
p=list(map(int,input().split()))
print(po(p,s))