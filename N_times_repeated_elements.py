def po(a,k):
    dic={}
    for i in a:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    c=[]
    for i in a:
        if dic[i]==k:
            if i not in c:
                c.append(i)
    if len(c)==0:
        return [-1]
    else:
        return c
    
    
a=int(input())
p=list(map(int,input().split()))
k=int(input())
print(*po(p,k))