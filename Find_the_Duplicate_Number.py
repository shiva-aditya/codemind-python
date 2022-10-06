def po(n,c):
    for i in range(0,c):
        if n.count(n[i])>1:
            return n[i]
    
    
    
f=int(input())
a=list(map(int,input().split()))
print(po(a,f))