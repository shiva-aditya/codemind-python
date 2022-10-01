n=[]
def po(a):
    a.sort()
    global n
    if len(a)==1:
        n.append(1)
        return n
    elif len(set(a))==1:
        n.append(len(a))
        return n
    else:
        n.append(len(a))
        m=min(a)
        for i in range(0,len(a)):
            a[i]=abs(m-a[i])
        for j in range(len(a)-1,-1,-1):
            if a[j]==0:
                a.remove(a[j])
        return po(a)



p=int(input())
h=list(map(int,input().split()))
o=po(h)
for _ in o:
    print(_)
