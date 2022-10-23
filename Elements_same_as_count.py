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
    else:
        return c
                
s=int(input())
q=list(map(int,input().split()))
print(*po(q))