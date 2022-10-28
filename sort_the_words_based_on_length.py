def po(n):
    n.sort()
    d=[]
    for i in n:
        d.append(len(i))
    d.sort()
    ans=[]
    for i in d:
        for j in n:
            if len(j)==i:
                ans.append(j)
                n.remove(j)
    return ans
    
p=input()
p=p.split()
print(*po(p))