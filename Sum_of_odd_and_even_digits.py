def po(n,l):
    e=0
    o=0
    for i in range(0,l):
        if i%2==0:
            e+=n[i]
        else:
            o+=n[i]
    if abs(e-o)==0:
        return "YES"
    else:
        return "NO"




s=int(input())
a=list(map(int,input().split()))
print(po(a,s))