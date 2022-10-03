def po(a,l,d):
    c=0
    s=0
    for i in range(0,l):
        if s>1:
            break
        elif a[i]>d:
            s+=1
        else:
            c+=1
    return c

d,f=map(int,input().split())
a=list(map(int,input().split()))
print(po(a,d,f))






d