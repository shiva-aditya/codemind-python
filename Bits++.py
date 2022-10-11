s=[]
ans=0
for _ in range(int(input())):
    s.append(input())
for i in s:
    if "+" in i:
        ans+=1
    else:
        ans-=1
print(ans)