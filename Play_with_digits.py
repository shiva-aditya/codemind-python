def po(a):
    c=0
    for i in a:
        p=mo(i)
        c+=p
    return c
    
    
def mo(a):
    e=[]
    while a:
        r=a%10
        a=a//10
        e.append(r)
    return sum(e)
    
    
    
s=int(input())
q=list(map(int,input().split()))
print(po(q))