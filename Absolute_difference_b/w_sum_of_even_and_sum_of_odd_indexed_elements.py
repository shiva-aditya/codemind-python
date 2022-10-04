b=int(input())
s=list(map(int,input().split()))
e=0
o=0
for i in range(0,b):
    if i%2==0:
        e+=s[i]
    else:
        o+=s[i]
print(abs(e-o))
        