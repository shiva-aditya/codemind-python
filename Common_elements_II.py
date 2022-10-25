def po(a,b):
    e=[]
    for i in a:
        if i not in e:
            e.append(i)
    o=[]
    for i in b:
        if i not in o:
            o.append(i)
    ans=[]
    for i in a:
        if i not in b:
            ans.append(i)
    for j in b:
        if j not in a:
            ans.append(j)
    return ans


a,b=map(int,input().split())
s=list(map(int,input().split()))
v=list(map(int,input().split()))
print(*po(s,v))