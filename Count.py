def po(a,b):
    e=0
    o=0
    for i in a:
        if i%2==0:
            e=e+1
        else:
            o=o+1
    return [e,o]
    
    
v=int(input())
b=list(map(int,input().split()))
print(*po(b,v))