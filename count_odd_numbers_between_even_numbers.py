def po(a,l):
    c=0
    for i in range(l-2):
        if a[i]%2==0 and a[i+2]%2==0 and a[i+1]%2!=0:
            c+=1
    return c
    
    
    
    
s=int(input())
d=list(map(int,input().split()))
print(po(d,s))