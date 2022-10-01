def po(n,m):
    a=0
    b=0
    for i in range(0,len(n)):
        if n[i] > m[i]:
            a=a+1
        elif n[i] < m[i]:
            b=b+1
        elif n[i] == m[i]:
            continue
    return a,b


a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(*po(a,b))