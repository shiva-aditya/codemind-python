def po(a):
    c=0
    for i in a:
        if i%2==0:
            return c
        else:
            c+=i
    return c

s=int(input())
q=list(map(int,input().split()))
print(po(q))