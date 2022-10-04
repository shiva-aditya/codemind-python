b=int(input())
s=list(map(int,input().split()))
e=0
o=0
for i in range(0,b):
    if s[i]%2!=0:
        e+=s[i]
print(e)