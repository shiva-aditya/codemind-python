def po(a):
    dic={}
    for i in a:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    c=[]
    for k in dic.keys():
        if dic[k]==1:
            c.append(k)
    c.sort()
    return c
w=input()
w=w.lower()
w=w.split()
w="".join(w)
p=po(w)
for i in p:
    print(i,end="")