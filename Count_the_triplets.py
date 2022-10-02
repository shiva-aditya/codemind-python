def po(a):
    a.sort()
    c=0
    for i in range(0,len(a)-1):
        for j in range(0,len(a)-1):
            if a[i]==a[j]:
                continue
            else:
                d=a[i]+a[j]
                if d in a:
                    c+=1
    if c==0:
        return -1
    else:
        return c//2
            
for _ in range(int(input())):
    e=int(input())
    d=list(map(int,input().split()))
    print(po(d))
