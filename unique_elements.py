def po(a):
    c=[]
    for i in a:
        if i not in c:
            c.append(i)
    return c
    
l=int(input())
e=list(map(int,input().split()))
print(*po(e))