def po(a):
    dic={}
    for i in a:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    c=[]
    for i in a:
        if dic[i]==i:
            if i not in c:
                c.append(i)
    if len(c)==0:
        return [-1]
    elif len(c)==1:
        return [c[0],c[0]]
    else:
        return min(c),max(c)
        
s=int(input())
q=list(map(int,input().split()))
print(*po(q))