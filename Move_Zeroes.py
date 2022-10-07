def po(a,l):
    for i in range(0,l):
        if a[i]==0:
            a.append(a[i])
            a.remove(a[i])
    return a




d=int(input())
a=list(map(int,input().split()))
print(*po(a,d))