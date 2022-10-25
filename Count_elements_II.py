def po(a,b):
    c=0
    for i in a:
        if i not in b:
            c+=1
    for j in b:
        if j not in a:
            c+=1
    return c






a,b=map(int,input().split())
n=list(set(map(int,input().split())))
m=list(set(map(int,input().split())))
print(po(n,m))