def po(a):
    c=[]
    for i in a:
        if i%2==0:
            if i not in c:
                c.append(i)
    return len(c)
    
s=int(input())
q=list(map(int,input().split()))
print(po(q))