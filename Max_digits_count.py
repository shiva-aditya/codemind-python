def po(a,l):
    d=[]
    for i in a:
        d.append(len(i))
    dic={}
    for i in d:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1#{2: 2, 3: 1, 1: 1, 4: 1}
    e=max(dic)
    return dic[e]
        
s=int(input())
q=list(map(str,input().split()))
print(po(q,s))
