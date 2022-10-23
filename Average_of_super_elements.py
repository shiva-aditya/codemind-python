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
        print(-1)
    else:
        s=sum(c)
        h=s/len(c)
        print("{:.2f}".format(h))

s=int(input())
w=list(map(int,input().split()))
po(w)