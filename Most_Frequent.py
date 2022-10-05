d=int(input())
s=list(map(int,input().split()))
dic={}
for i in s:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
n=[]
m=[]
for k,v in dic.items():
    n.append(k)
    m.append(v)
w=max(m)
x=m.index(w)
print(n[x])
    