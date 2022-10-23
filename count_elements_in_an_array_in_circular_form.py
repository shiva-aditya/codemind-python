def po(a):
    a.extend(a[:2:])
    c=0
    for i in range(0,len(a)-2):
        if a[i]%2==0 and a[i+2]%2!=0 or a[i]%2!=0 and a[i+2]%2==0:
            c+=1
    return c

s=int(input())
p=list(map(int,input().split()))
print(po(p))