l,r=map(int,input().split())
a=list(map(int,input().split()))
x=a[:r:]
d=l-r
s=a[::-1]
ans=[]
for i in range(d):
    ans.append(s[i])
ss=ans[::-1]
ss.extend(x)
print(*ss)

