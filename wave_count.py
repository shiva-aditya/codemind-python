def po(a,l):
    c=0
    for i in range(0,l-2,2):
        if a[i]<a[i+1] and a[i+1]>a[i+2]:
            pass
        else:
            return -1
    for i in range(0,l-2,2):
        if a[i]<a[i+1] and a[i+1]>a[i+2]:
            c+=1
    return c
    
s=int(input())
q=list(map(int,input().split()))
print(po(q,s))