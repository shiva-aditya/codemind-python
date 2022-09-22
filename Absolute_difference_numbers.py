def po(a,b):
    p=str(a)
    d=int(p[:b:])
    u=int(p[-b::])
    return abs(d-u)

    
    
n,m=map(int,input().split())
print(po(n,m))
