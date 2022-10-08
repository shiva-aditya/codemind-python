def po(a,l):
    n=0
    m=0
    for i in range(l):
        if i%2!=0:
            n+=a[i]
        else:
            m+=a[i]
    if (n-m)%4==0:
        return "X"
    else:
        return "Y"


s=int(input())
n=list(map(int,input().split()))
print(po(n,s))