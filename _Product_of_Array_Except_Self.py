def po(a,b):
    f=[]
    for i in range(0,b):
        c=1
        for j in range(0,b):
            if a[j]==a[i]:
                continue
            else:
                c=c*a[j]
        f.append(c)
    return f
s=int(input())
p=list(map(int,input().split()))
print(*po(p,s))