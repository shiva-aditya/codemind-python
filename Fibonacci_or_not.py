d=int(input())
f=[0,1]
c=0
for i in range(2,d):
    v=f[::-1]
    c=v[0]+v[1]
    f.append(c)
if d in f:
    print(True)
else:
    print(False)