def po(a,l):
    c=1
    for i in range(1,l):
        if a[i]<a[i-1]:
            c+=1
        else:
            continue
    return c


for _ in range(int(input())):
    d=int(input())
    q=list(map(int,input().split()))
    print(po(q,d))