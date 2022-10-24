def po(a):
    dic={}
    for i in a:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    c=0
    for k in dic.keys():
        c+=k
    return c

s=int(input())
q=list(map(int,input().split()))
print(po(q))